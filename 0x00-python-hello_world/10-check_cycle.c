#include "lists.h"

/**
 * check_cycle - Function that checks if a list has a cycle
 *
 * @list: A singly linked list
 *
 * Return: 0 (SUCCESS) ther is no cycle, 0 (Failure) otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *next;

	if (list == NULL || list->next == NULL)
                return (0);
	head = list;
	next = list->next;
	while (head != NULL && next->next != NULL)
	{
		if (head == next)
			return (1);
		head = head->next;
		next = next->next->next;
	}

	return (0);
}
