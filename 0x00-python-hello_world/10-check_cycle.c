#include "lists.h"

/**
 * check_cylce - check if linked list has a cycle
 * @list: linked list to be checked
 * Description: Uses Floyd's cycle finding algorithm to check for a cycle
 * Return: 1 if true_cycle, 0 if false_no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (list == NULL)
		return (0);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
