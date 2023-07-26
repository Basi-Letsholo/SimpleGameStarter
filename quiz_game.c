#include "main.h"

/**
 * quiz_game - General Knowledge quiz
 */
int quiz_game(void)
{
	char *questions[ARRAY_SIZE], *answers, temp = "";
	int i, num_questions = 0;

	questions[0] = "What is the capital city of France?";
	questions[1] = "Who wrote the play 'Romeo and Juliet'?";
	questions[2] = "Which planet is known as the 'Red Planet'?";
	questions[3] = "What is the largest mammal on Earth?";
	questions[4] = "How many continents are there in the world?";
	questions[5] = '\0';

	i = 0;
	while (questions[i] != NULL) 
	{
		num_questions++;
		i++;
	}

	answers = malloc(sizeof(char) * num_questions);
	if (answers == NULL)
	{
		return (-1);
	}

	printf("----- General Knowledge Quiz -----\n");

	printf("%d\n", num_questions);
	for (i = 0; i < num_questions; i++)
	{
		printf("------------------\n");
		printf("%s\n", questions[i]);
		scanf("%s", &temp);
		strcpy(temp, answers[i]);
	}

	for (i = 0; i < num_questions; i++)
	{
		printf("%s\n", answers[i]);
	}

	free(answers);
	return (0);
}

int main(void)
{
	quiz_game();

	return (0);
}
