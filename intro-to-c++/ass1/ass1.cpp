/*Assignment 1
Name: Daim Bin Khalid
Roll no: 251686775*/

#include <iostream>
#include <cstdlib>
#include <conio.h>

using namespace std;

// define arrow keys for user input
#define up 72
#define down 80
#define left 75
#define right 77

// global variables
int grid[4][4] = {0}; // global grid
int tile_counter = 0; // occupied tile counter
int score = 0, high_score = 0;
int largest_tile;       // var to store largest tile score
bool game_over = false; // bool for running main loop

// func to check if any moves are left
// called in generate_tile()
bool check_game_over()
{
    // Check for available moves
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            // Check for empty cells
            if (grid[i][j] == 0)
            {
                return false;
            }

            // Check for adjacent cells with the same value
            if ((i < 4 - 1 && grid[i][j] == grid[i + 1][j]) ||
                (j < 4 - 1 && grid[i][j] == grid[i][j + 1]))
            {
                return false;
            }
        }
    }

    // No available moves left
    return true;
}

void generate_tile()
{
    // check to see if grid is full (no moves left)
    if (tile_counter == 16 && check_game_over())
    {
        game_over = true;
        return;
    }

    // get grid coordinates for rand empty tile
    int i = rand() % 4;
    int j = rand() % 4;
    while (grid[i][j] != 0)
    {
        i = rand() % 4;
        j = rand() % 4;
    }

    // get tile score
    int tile_score = rand() % 2;
    if (tile_score == 0)
    {
        tile_score = 2;
        grid[i][j] = tile_score;
        tile_counter++;
    }
    else
    {
        tile_score = 4;
        grid[i][j] = tile_score;
        tile_counter++;
    }
}

// movement functions
void move_right()
{
    // move tiles to the right and merge adjacent tiles of the same value
    for (int i = 0; i < 4; i++)
    {
        for (int j = 2; j >= 0; j--)
        {
            if (grid[i][j] != 0)
            {
                int k = j;
                while (k < 3 && grid[i][k + 1] == 0)
                {
                    grid[i][k + 1] = grid[i][k];
                    // reset previous merged value to zero
                    grid[i][k] = 0;
                    k++;
                }

                if (k < 3 && grid[i][k + 1] == grid[i][k])
                {
                    grid[i][k + 1] *= 2;
                    grid[i][k] = 0;
                    tile_counter--;

                    // update score
                    score += grid[i][k + 1];
                }
            }
        }
    }

    // generate new tile
    generate_tile();
}

void move_up()
{
    // move tiles up and merge adjacent tiles of the same value
    for (int j = 0; j < 4; j++)
    {
        for (int i = 1; i < 4; i++)
        {
            if (grid[i][j] != 0)
            {
                int k = i;
                while (k > 0 && grid[k - 1][j] == 0)
                {
                    grid[k - 1][j] = grid[k][j];
                    grid[k][j] = 0;
                    k--;
                }

                if (k > 0 && grid[k - 1][j] == grid[k][j])
                {
                    grid[k - 1][j] *= 2;
                    grid[k][j] = 0;
                    tile_counter--;

                    // update score
                    score += grid[k - 1][j];
                }
            }
        }
    }

    // generate new tile
    generate_tile();
}

void move_down()
{
    for (int j = 0; j < 4; j++)
    {
        for (int i = 2; i >= 0; i--)
        {
            if (grid[i][j] != 0)
            {
                int k = i + 1;
                while (k < 4 && grid[k][j] == 0)
                {
                    k++;
                }

                if (k - 1 != i)
                {
                    grid[k - 1][j] = grid[i][j];
                    grid[i][j] = 0;
                }

                if (k < 4 && grid[k][j] == grid[k - 1][j])
                {
                    grid[k][j] *= 2;
                    grid[k - 1][j] = 0;
                    tile_counter--;

                    // update score
                    score += grid[k][j];
                }
            }
        }
    }

    // generate new tile
    generate_tile();
}

void move_left()
{
    for (int j = 0; j < 4; j++)
    {
        for (int i = 0; i < 4; i++)
        {
            // swap i and j to update the correct element
            if (grid[j][i] != 0)
            {
                int k = i - 1;
                while (k >= 0 && grid[j][k] == 0)
                {
                    k--;
                }

                if (k + 1 != i)
                {
                    grid[j][k + 1] = grid[j][i];
                    grid[j][i] = 0;
                }

                if (k >= 0 && grid[j][k] == grid[j][k + 1])
                {
                    grid[j][k] *= 2;
                    grid[j][k + 1] = 0;
                    tile_counter--;

                    // update score
                    score += grid[j][k];
                }
            }
        }
    }

    // generate new tile
    generate_tile();
}

void get_largest_tile()
{
    // func to get the largest tile in the grid
    int largest_tile;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (largest_tile < grid[i][j])
            {
                largest_tile = grid[i][j];
            }
        }
    }
}

void display_grid()
{
    // using printf to have formatting in display using %4d
    // print top border line
    printf("/------|------|------|------\\\n");

    for (int i = 0; i < 4; i++)
    {
        // print left border line
        printf("|");

        for (int j = 0; j < 4; j++)
        {
            // print cell value with fixed width
            printf(" %4d ", grid[i][j]);

            // add right border line
            printf("|");
        }

        // print new line and bottom border line
        printf("\n");
        if (i != 3)
        {
            printf("|------|------|------|------|\n");
        }
    }
    printf("\\------|------|------|------/\n");
}

int main()
{
    // set seed
    srand(time(0));
    // initialize first two tiles
    generate_tile();
    generate_tile();

    int user_input = 0;
    bool exit_game = false;
    string play_again;

    while (!exit_game)
    {
        system("cls");
        display_grid();
        // print score and high score
        cout << "Score: " << score << endl;
        cout << "High Score: " << high_score << endl;
        cout << "Press any arrow key: ";

        // switch case for arrow input
        switch ((user_input = getch()))
        {
        case up:
            move_up();
            break;
        case down:
            move_down();
            break;
        case left:
            move_left();
            break;
        case right:
            move_right();
            break;
        }

        if (game_over == true)
        {
            high_score = score;
            system("cls");
            display_grid();
            // print score and high score
            cout << "Score: " << score << endl;
            cout << "High Score: " << high_score << endl;
            cout << "Game Over" << endl;

            // play again logic
            cout << "Play Again? (Y/N) " << endl;
            cin >> play_again;
            if (play_again == "y" || play_again == "Y")
            {
                // reset the grid
                for (int i = 0; i < 4; i++)
                {
                    for (int j = 0; j < 4; j++)
                    {
                        grid[i][j] = 0;
                    }
                }
                // reset the score
                score = 0;
                largest_tile = 0;
                game_over = false;
                // generate new tiles
                generate_tile();
                generate_tile();
            }
            else if (play_again == "n" || play_again == "N")
            {
                exit_game = true;
            }
        }
        else if (largest_tile >= 2048)
        {
            high_score = score;
            system("cls");
            display_grid();
            cout << "High Score: " << high_score << endl;
            cout << "\nYou Won!" << endl;
            cout << "Winning Score: " << score << endl;

            // play again logic
            cout << "Play Again? (Y/N) " << endl;
            cin >> play_again;
            if (play_again == "y" || play_again == "Y")
            {
                // reset the grid
                for (int i = 0; i < 4; i++)
                {
                    for (int j = 0; j < 4; j++)
                    {
                        grid[i][j] = 0;
                    }
                }
                // reset the score
                score = 0;
                largest_tile = 0;
                game_over = false;
                // generate new tiles
                generate_tile();
                generate_tile();
            }
            else if (play_again == "n" || play_again == "N")
            {
                exit_game = true;
            }
        }
    }

    return 0;
}
