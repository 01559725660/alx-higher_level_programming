int palindrome(listint_t **j, listint_t *i)
{
	int i;

	if (i != NULL)
	{
		i = palindrome(j, i->next);
		if (i != 0)
		{
			i = (i->n == (*j)->n);
			*j = (*j)->next;
			return (i);
		}
		return (0);

	}
	return (1);
}

int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
