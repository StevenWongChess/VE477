#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 

typedef struct _Edge 
{ 
	int start, end, weight; 
}Edge; 

typedef struct _Graph 
{ 
	// V number of vertices, E number of edges 
	int V, E; 
	Edge* edge; 
}Graph; 

Graph* createGraph(int V, int E) 
{ 
	Graph* graph = (Graph*) malloc(sizeof(Graph)); 
	graph->V = V; 
	graph->E = E; 
	graph->edge = (Edge*) malloc(E * sizeof(Edge));
	return graph; 
}

typedef struct _Subset 
{ 
	int parent; 
	int rank; 
}Subset; 

//for qsort
int Comp(const void* a, const void* b) 
{ 
	Edge* a1 = (Edge*)a; 
	Edge* b1 = (Edge*)b; 
	return a1->weight - b1->weight; 
} 

int Comp2(const void* a, const void* b) // only for joj format
{ 
	Edge* a1 = (Edge*)a; 
	Edge* b1 = (Edge*)b; 
	if (a1->start == b1->start){
		return a1->end - b1->end;
	}
	return a1->start - b1->start;
} 

void PrimMST(Graph *graph){

	int V = graph->V; 
	Edge result[V];
	int e = 0;

    qsort(graph->edge,graph->E,sizeof(Edge),Comp);
    int *connected = malloc(graph->E*sizeof(int));

    for (int i = 0; i < V; i++) 
    	connected[i] = 0;

    connected[graph->edge[0].start] = 1;
    for (int i = 0; i < V; i++){
        for (int j = 0; j < graph->E; j++){
            if (connected[graph->edge[j].start] + connected[graph->edge[j].end] == 1){
                result[i] = graph->edge[j];
                e++;
                connected[result[i].start] = 1;
                connected[result[i].end] = 1;
                break;
            }
        }
    }

    qsort(result, e, sizeof(Edge), Comp2);
	for (int i = 0; i < e; i++) 
		printf("%d--%d\n", result[i].start, result[i].end); 
    free(connected);
}

int main() 
{ 
	int V = 0; // Number of vertices in graph 
	int E = 0; // Number of edges in graph 
	scanf("%d", &E);
	scanf("%d", &V);
	Graph* graph = createGraph(V, E);
	//printf("%d %d\n", V, E);
	for(int i = 0; i < E; i++){
		int a; 
		int b; 
		scanf("%d %d %d", &a, &b, &graph->edge[i].weight);
		if (a<b){
			graph->edge[i].start = a;
			graph->edge[i].end = b;
		}
		else{
			graph->edge[i].start = b;
			graph->edge[i].end = a;
		}
		//printf("%d %d %d\n ", a, b, graph->edge[i].weight);
	}
	PrimMST(graph); 
	free(graph);

	return 0; 
} 

