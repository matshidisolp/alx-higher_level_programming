 22 /*int cycle_check(listint_t *list)
 23 {
 24         listint_t *slow = list;
 25         listint_t *fast = list;
 26
 27         if (list == NULL)
 28                 return (0);
 29         while (fast && fast->next)
 30         {
 31                 slow = slow->next;
 32                 fast = fast->next->next;
 33                 if (slow == fast)
 34                         return(1);
 35         }
 36         return (0);
 37 }*/
