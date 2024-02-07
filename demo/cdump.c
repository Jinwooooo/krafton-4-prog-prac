#include "rbtree.h"

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

rbtree *new_rbtree(void) {
  rbtree *t = (rbtree *)calloc(1, sizeof(rbtree));
  t->nil = (node_t *)calloc(1, sizeof(node_t));
  t->nil->color = RBTREE_BLACK;
  t->root = t->nil;
  return t;
}

// [MOD] added to delete node within the RB Tree
void delete_node(rbtree *t, node_t *curr) {
  if (curr != t->nil) {
    delete_node(t, curr->left);
    delete_node(t, curr->right);
    free(curr);
  }
}

void delete_rbtree(rbtree *t) {
  delete_node(t, t->root);
  free(t->nil);
  free(t);
}

// [MOD] rotating a sub-tree left (modular function for insert/delete reuse purposes)
void rotate_left(rbtree *t, node_t *curr) {
  node_t *r = curr->right;
  curr->right = r->left;

  if(r->left != t->nil) {
    r->left->parent = curr;
  }

  r->parent = curr->parent;

  if(curr->parent == t->nil) {
    t->root = r;
  } else if(curr == curr->parent->left) {
    curr->parent->left = r;
  } else {
    curr->parent->right = r;
  }

  r->left = curr;
  curr->parent = r;
}

// [MOD] rotating a sub-tree left (modular function for insert/delete reuse purposes)
void rotate_right(rbtree *t, node_t *curr) {
  node_t *l = curr->left;
  curr->left = l->right;

  if(l->right != t->nil) {
    l->right->parent = curr;
  }

  l->parent = curr->parent;

  if(l->parent == t->nil) {
    t->root = l;
  } else if(curr == curr->parent->right) {
    curr->parent->right = l;
  } else {
    curr->parent->left = l;
  }

  l->right = curr;
  curr->parent = l;
}

// [MOD] recoloring and/or restructuring tree to make sure the 5 rules of RBTree are maintained
// void insert_fix(rbtree *t, node_t *curr) {
//   node_t *curr_parent;
//   node_t *curr_grand;
//   int temp_color;

//   while((curr != t->root) && (curr->color != RBTREE_BLACK) && (curr->parent->color == RBTREE_RED)) {
//     curr_parent = curr->parent;
//     curr_grand = curr->parent->parent;

//     if(curr->parent == curr_grand->right) {
//       node_t *curr_uncle = curr_grand->left;
//       // case 1r: grand right parent + uncle red -> RECOLOR
//       if ((curr_uncle != NULL) && (curr_uncle->color == RBTREE_RED)) {
//         curr_grand->color = RBTREE_RED;
//         curr_parent->color = RBTREE_BLACK;
//         curr_uncle->color = RBTREE_BLACK;
//         curr = curr_grand;
//       // case 2r: grand right parent + uncle black + parent left -> RESTRUCTURE 1
//       } else {
//         if(curr == curr_parent->left) {
//           rotate_right(t, curr_parent);
//           curr = curr_parent;
//           curr_parent = curr->parent;
//         }
//         // case 3r: grand right parent + uncle black + parent right -> RESTRUCTURE 2
//         rotate_left(t, curr_grand);
//         curr_parent->color = curr_grand->color;
//         curr_grand->color = temp_color;
//         curr = curr_parent;
//       }
//     } else {
//       node_t *curr_uncle = curr_grand->right;
//       // case 1l: grand left parent + uncle red -> RECOLOR
//       if(curr_uncle != NULL && curr_uncle->color == RBTREE_RED) {
//         curr_grand->color = RBTREE_RED;
//         curr_parent->color = RBTREE_BLACK;
//         curr_uncle->color = RBTREE_BLACK;
//         curr = curr_grand;
//       // case 2l: grand right parent + uncle black + parent right -> RESTRUCTURE 2
//       } else {
//         if (curr == curr_parent->right) {
//           rotate_left(t, curr_parent);
//           curr = curr_parent;
//           curr_parent = curr->parent;
//         }
//         // case 3l: grand right parent + uncle black + parent left -> RESTRUCTURE 1
//         rotate_right(t, curr_grand);
//         curr_parent->color = curr_grand->color;
//         curr_grand->color = temp_color;
//         curr = curr_parent;
//       }
      
//     }

//     if(curr == t->root) {
//         break;
//     }

//     // because root must be black
//     t->root->color = RBTREE_BLACK;
//   }
// }

void insert_fix(rbtree *t, node_t *curr) {
  while(curr != t->root && curr->parent->color == RBTREE_RED) {
    node_t *curr_parent = curr->parent;
    node_t *curr_grand = curr_parent->parent;

    if(curr_parent == curr_grand->left) {
      node_t *curr_uncle = curr_grand->right;

      if(curr_uncle != NULL && curr_uncle->color == RBTREE_RED) {
        curr_grand->color = RBTREE_RED;
        curr_parent->color = RBTREE_BLACK;
        curr_uncle->color = RBTREE_BLACK;
        curr = curr_grand;
      } else {
        if(curr == curr_parent->right) {
          rotate_left(t, curr_parent);
          curr = curr_parent;
        }

        curr_parent = curr->parent;
        curr_grand = curr_parent->parent;
        curr_parent->color = RBTREE_BLACK;
        curr_grand->color = RBTREE_RED;
        rotate_right(t, curr_grand);
      }
    } else {
      node_t *curr_uncle = curr_grand->left;

      if(curr_uncle != NULL && curr_uncle->color == RBTREE_RED) {
        curr_grand->color = RBTREE_RED;
        curr_parent->color = RBTREE_BLACK;
        curr_uncle->color = RBTREE_BLACK;
        curr = curr_grand;
      } else {
        if(curr == curr_parent->left) {
          rotate_right(t, curr_parent);
          curr = curr_parent;
        }

        curr_parent = curr->parent;
        curr_grand = curr_parent->parent;
        curr_parent->color = RBTREE_BLACK;
        curr_grand->color = RBTREE_RED;
        rotate_left(t, curr_grand);
      }
    }
  }
  t->root->color = RBTREE_BLACK;
}



node_t *rbtree_insert(rbtree *t, const key_t key) {
  node_t *node = (node_t *)calloc(1, sizeof(node_t));
  node->key = key;
  node->color = RBTREE_RED;
  node->parent = t->nil;
  node->left = t->nil;
  node->right = t->nil;

  node_t *parent_position = t->nil;
  node_t *insert_position = t->root;

  // finding node insert position
  while(insert_position != t->nil) {
    // saving parent position for later use
    parent_position = insert_position;
    if(node->key < insert_position->key) {
      insert_position = insert_position->left;
    } else {
      insert_position = insert_position->right;
    }
  }

  node->parent = parent_position;
  if(parent_position == t->nil) {
    t->root = node;
  } else if(node->key < parent_position->key) {
    parent_position->left = node;
  } else {
    parent_position->right = node;
  }

  // checking cases for when insert_fix is not necessary
  if(node->parent == t->nil) {
    node->color = RBTREE_BLACK;
    return node;
  }
  if(node->parent->parent == NULL) {
    return node;
  }

  insert_fix(t, node);
  return node;
}

node_t *rbtree_find(const rbtree *t, const key_t key) {
  node_t *curr = t->root;

  while(curr != t->nil) {
    if(curr->key > key) {
      curr = curr->left;
    } else if(curr->key < key) {
      curr = curr->right;
    } else {
      return curr;
    }
  }

  return NULL;
}

node_t *rbtree_min(const rbtree *t) {
  node_t *min = t->root;

  if(min == t->nil) {
    return NULL;
  }

  while(min->left != t->nil) {
    min = min->left;
  }

  return min;
}

node_t *rbtree_max(const rbtree *t) {
  node_t *max = t->root;

  if(max == t->nil) {
    return NULL;
  }

  while(max->right != t->nil){
    max = max->right;
  }

  return max;
}

void transplant(rbtree *t, node_t *node_del, node_t *node_sub) {
  if(node_del == NULL || node_sub == NULL) {
    return;
  }

  if(node_del->parent == t->nil) {
    t->root = node_sub;
  } else if(node_del->parent->left == node_del) {
    node_del->parent->left = node_sub;
  } else {
    node_del->parent->left = node_sub;
  }

  node_sub->parent = node_del->parent;
}

node_t *sub_minimum(rbtree *t, node_t *curr) {
  if(curr == NULL) {
    return NULL;
  }

  while(curr->left != t->nil) {
    curr = curr->left;
  }
  return curr;
}

// [MOD] recoloring and/or restructuring tree to make sure the 5 rules of RBTree are maintained
void erase_fix(rbtree *t, node_t *curr) {
  if(curr == NULL) {
    return;
  }

  node_t *sibling;

  while(curr != t->root && curr->color == RBTREE_BLACK) {
    if(curr->parent && curr == curr->parent->left) {
      sibling = curr->parent->right;
      if(sibling && sibling->color == RBTREE_RED) {
        sibling->color = RBTREE_BLACK;
        curr->parent->color = RBTREE_RED;
        rotate_left(t, curr->parent);
        sibling = curr->parent->right;
      }

      if(sibling && sibling->left && sibling->right && sibling->left->color == RBTREE_BLACK && sibling->right->color == RBTREE_BLACK) {
        sibling->color = RBTREE_RED;
        curr = curr->parent;
      } else {
        if(sibling && sibling->right && sibling->right->color == RBTREE_BLACK) {
          sibling->left->color = RBTREE_BLACK;
          sibling->color = RBTREE_RED;
          rotate_right(t, sibling);
          sibling = curr->parent->right;
        }

        sibling->color = curr->parent->color;
        curr->parent->color = RBTREE_BLACK;
        sibling->right->color = RBTREE_BLACK;
        rotate_left(t, curr->parent);
        curr = t->root;
      }
    } else {
      sibling = curr->parent->left;
      if(sibling->color == RBTREE_RED) {
        sibling->color = RBTREE_BLACK;
        curr->parent->color = RBTREE_RED;
        rotate_right(t, curr->parent);
        sibling = curr->parent->left;
      }

      if(sibling && sibling->right && sibling->left && sibling->right->color == RBTREE_BLACK && sibling->left->color == RBTREE_BLACK) {
        sibling->color = RBTREE_RED;
        curr = curr->parent;
      } else {
        if(sibling && sibling->left && sibling->left->color == RBTREE_BLACK) {
          sibling->right->color = RBTREE_BLACK;
          sibling->color = RBTREE_RED;
          rotate_left(t, sibling);
          sibling = curr->parent->left;
        }

        sibling->color = curr->parent->color;
        curr->parent->color = RBTREE_BLACK;
        sibling->left->color = RBTREE_BLACK;
        rotate_right(t, curr->parent);
        curr = t->root;
      }
    }
  }

  curr->color = RBTREE_BLACK;
}

int rbtree_erase(rbtree *t, node_t *curr) {
  if(curr == NULL) {
    return -1;
  }

  node_t *node_rep;
  node_t *node_ref = curr;
  int o_color = node_ref->color;

  if(curr->left == t->nil) {
    node_rep = curr->right;
    if(node_rep) {
      transplant(t, curr, curr->right);
    }
  } else if (curr->right == t->nil) {
    node_rep = curr->left;
    if(node_rep) {
      transplant(t, curr, curr->left);
    }
  } else {
    node_ref = sub_minimum(t, curr->right);
    if(node_ref) {
      o_color = node_ref->color;
      node_rep = node_ref->right;

      if(node_rep) {
        if(node_ref->parent == curr) {
          node_rep->parent = node_ref;
        } else {
          transplant(t, node_ref, node_ref->right);
          node_ref->right = curr->right;
          if(node_ref->right) {
            node_ref->right->parent = node_ref;
          }
        }
      }
      transplant(t, curr, node_ref);
      node_ref->left = curr->left;
      if(node_ref->left) {
        node_ref->left->parent = node_ref;
      }
      node_ref->color = curr->color;
    } 
  }

  if(o_color == RBTREE_BLACK) {
    erase_fix(t, node_rep);
  }
  free(curr);

  return 0;
}


int rbtree_to_array(const rbtree *t, key_t *arr, const size_t n) {
  // TODO: implement to_array
  return 0;
}

void print_helper(rbtree *t, node_t *node, char *indent, int last) {
    if(node != t->nil) {
        printf("%s", indent);
        if(last) {
            printf("R----");
            indent = strcat(indent, "     ");
        } else {
            printf("L----");
            indent = strcat(indent, "|    ");
        }

        char *s_color = (node->color == RBTREE_RED) ? "Red" : "Black";
        printf("%d (%s)\n", node->key, s_color);
        print_helper(t, node->left, indent, 0);
        print_helper(t, node->right, indent, 1);
    }
}

void print_tree(rbtree *t) {
    char *indent = malloc(1000 * sizeof(char)); // Allocate a buffer for the indent string
    indent[0] = '\0'; // Start with an empty string
    print_helper(t, t->root, indent, 1);
    free(indent); // Don't forget to free the buffer when you're done with it
}


int main(int argc, char *argv[]) {
  rbtree *t = new_rbtree();
  for(int i = 1; i < 11; i++) {
    rbtree_insert(t, i);
  }
  
  print_tree(t);
}
