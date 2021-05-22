#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include "hash.h"
https://stackoverflow.com/questions/51448301/why-use-malloc-when-i-can-just-define-a-variable-length-array
typedef struct node_t {
   int key;
   int value;	
   struct node_t *next;
   //struct node_t *prev;
} node;

/* terrible time complexity O(n^2)
node *nth_entry(ht *table, int size, int key){

	int hash_code = key % size;
	sll *probe = table->head;
	for(int i = 0; i < hash_code; i++){
		probe = probe->next;
	}
	return probe->head;
}*/

void *initializer(int size){// int array[n] is not allowed, so trick is used rather than array
	size = size / 3;
	node **hash = (node **)malloc(sizeof(node*)*size);
	for (int i = 0; i < size; i++){
		hash[i] = (node *)malloc(sizeof(node));
		hash[i]->next = NULL;
	}
	return hash;
}

void insert(void* hashtable, int size, int key, int value){
	size = size / 3;
	node **hash = hashtable;
	node *probe = hash[key % size];
	while (probe->next != NULL){
		probe = probe->next;
		if(probe->key == key){
			probe->value = value;
			return;
		}
	}
	probe->next = (node *)malloc(sizeof(node));
	probe = probe->next;
    probe->key = key;
    probe->value = value;
    probe->next = NULL;
}

void delete(void* hashtable, int size, int key){
	size = size / 3;
	node **hash = hashtable;
	node *probe = hash[key % size];
	while (probe->next != NULL){
		if(probe->next->key == key){
			node *temp = probe->next;
			probe->next = probe->next->next;
			free(temp);
			break;
		}
		probe = probe->next;
	}
}

void* search(void* hashtable, int size, int key){
	size = size / 3;
	node **hash = hashtable;
	node *probe = hash[key % size];
	while (probe->next != NULL){
		probe = probe->next;
		if(probe->key == key){
			return probe;
		}
	}
	return NULL;
}

int getValue(void* element){
	node *ele = element;
	return ele->value;
}

void freeHashtable(void* hashtable, int size){
	size = size / 3;
	node **hash = hashtable;

	for(int i = 0; i < size; i ++){
		node *ele = hash[i];
		node *temp;
		while(ele != NULL){
			temp = ele;
			ele = ele->next;
			free(temp);
		}
	}
	free(hash);
}

