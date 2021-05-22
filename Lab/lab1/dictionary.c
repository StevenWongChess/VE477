#include "dictionary.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct node_t {
   int key;
   int value;	
   struct node_t *next;
   struct node_t *prev;
} node;

typedef struct double_link_list
{
	node *head;
	node *tail;
} dll;

void *initializer(){//from head 0 to tail 10000 
	//to make life easier, head and tail are useless and we have n+2 elements
	dll *dict = (dll *)malloc(sizeof(dll));
	dict->head = (node *)malloc(sizeof(node));
	dict->tail = (node *)malloc(sizeof(node));

	dict->head->prev = NULL;
	dict->head->next = dict->tail;
	dict->tail->prev = dict->head;
	dict->tail->next = NULL;
	return dict;
}
void *search(void* dictionary, int key){
	dll *dict = dictionary;
	node *probe = dict->head->next;
	while(probe != dict->tail){
		if(probe->key == key){
			return probe;
		}
		else if(probe->key < key)
		{
			probe = probe->next;
		}
		else{
			return NULL;
		}
	}
	return NULL;
}
void insert(void* dictionary, int key, int value){
//https://stackoverflow.com/questions/59254661/segmentation-fault-with-null-pointer
	//printf("00");
	dll *dict = dictionary;
	node *probe = dict->head;
	while(probe != dict->tail){
		if(probe->next == dict->tail || probe->next->key > key){
			node *ele = (node *)malloc(sizeof(node));
			ele->prev = probe;
			ele->next = probe->next;
			probe->next->prev = ele; //order is vital
			probe->next = ele;

			ele->key = key;
			ele->value = value;
			//printf("11");
			break;
		}
		else if(probe->next->key == key)
		{
			probe->next->value = value;
			//printf("22");
			break;
		}
		else{
			probe = probe->next;
		}
	}
}
void delete(void* dictionary,int key){
	dll *dict = dictionary;
	node *probe = dict->head->next;
	while(probe != dict->tail){
		if(probe->key == key){
			node *p = probe;
			p->prev->next = p->next;
			p->next->prev = p->prev;
			free(p);
			break;
		}
		else
		{
			probe = probe->next;
		}
	}
}
void *minimum(void* dictionary){
	dll *dict = dictionary;
	if (dict->head->next == dict->tail)
		return NULL;
	else
		return dict->head->next;
}
void *maximum(void* dictionary){
	dll *dict = dictionary;
	if (dict->tail->prev == dict->head)
		return NULL;
	else
		return dict->tail->prev;
}
void *predecessor(void* dictionary, int key){
	dll *dict = dictionary;
	node *ele = search(dict, key);
	if (ele->prev == dict->head)
		return NULL;
	return ele->prev;
}
void *successor(void* dictionary, int key){
	dll *dict = dictionary;
	node *ele = search(dict, key);
	if (ele->next == dict->tail)
		return NULL;
	return ele->next;
}
int getkey(void* element){
	node *ele = element;
	return ele->key;
}
int getvalue(void* element){
	node *ele = element;	
	return ele->value;
}
void free_dict(void* dictionary){
	dll *dict = dictionary;
	node *probe = dict->head->next;
	node *next_probe;
	while (probe != dict->tail){
		next_probe = probe->next; 
		free(probe);
		probe = next_probe;
	}
	free(dict->tail);
	free(dict->head);
	free(dict);
}







