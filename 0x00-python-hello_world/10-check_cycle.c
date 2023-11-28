#include "lists.h"

/**
 * cycle_check - check if linked list has a cycle
 * @head: linked list to be checked
 * Description: Uses Floyd's cycle finding algorithm to check for a cycle
 * Return: 1 if true_cycle, 0 if false_no cycle
 */
int cycle_check(listint_t *head)
{
	listint_t *slow = head;
	listint_t *fast = head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
