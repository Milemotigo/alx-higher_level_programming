#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/*
int check_cycle(listint_t *list)
{
	listint_t *list;
	listint_t *head, current;
	head = current;

	if (head == NULL)
		current = head->next;
		head = current->next;
	//head = current->next;
	while(list)
	{
		current = current->next;
	}
	return(0);
}*/
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *tortoise, *hare;

    tortoise = list;
    hare = list;

    while (tortoise && hare && hare->next)
    {
        tortoise = tortoise->next;
        hare = hare->next->next;

        if (tortoise == hare)
            return (1);
    }

    return (0);
}
