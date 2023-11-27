#include "lists.h"

/**
 * cycle_check - check if linked list has a cycle
 * @list: linked list to be checked
 * Description: Uses Floyd's cycle finding algorithm to check for a cycle
 * Return: 1 if true_cycle, 0 if false_no cycle
 */
int cycle_check(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return(1);
	}
	return (0);
}
