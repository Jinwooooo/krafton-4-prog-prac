#include <stdio.h>
#include <stdlib.h>

struct node {
  int data;
  struct node *next;
};

void printLinkedlist(struct node *p) {
  while (p != NULL) {
    printf("%d\n", p->data);
    p = p->next;
  }
}

// inserting data into the front of the linked list
void push(struct node **head_ref, int new_data) {
    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = new_data; // insert data
    new_node->next = (*head_ref); // next node as head
    (*head_ref) = new_node; // head to new node
}

void insertAfter(struct node *prev_node, int new_data)
{
    // 나한테 연결될 노드가 NULL인지 확인 (없으면 연결 못함)
    if (prev_node == NULL) {
        return;
    }

    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = new_data;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
}

void append(struct node **head_ref, int new_data)
{
    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    struct node *last = *head_ref;

    new_node->data = new_data;
    new_node->next = NULL; // 꼬리는 NULL
 
 	// 마지막 노드까지 순환
    while (last->next != NULL)
        last = last->next;
 
    // 도착시 변경
    last->next = new_node;
}

int main(void) {
	/* Initialize nodes */
	struct node *head;
	struct node *one = NULL;
	struct node *two = NULL;
	struct node *three = NULL;

	/* Allocate memory */
	one = malloc(sizeof(struct node));
	two = malloc(sizeof(struct node));
	three = malloc(sizeof(struct node));

	/* Assign data values */
	one->data = 1;
	two->data = 2;
	three->data = 3;

	/* Connect nodes */
	one->next = two;
	two->next = three;
	three->next = NULL;

	/* Save address of first node in head */
	head = one;
	printLinkedlist(head);
}