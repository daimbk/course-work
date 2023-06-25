#include "media.h"
#include <iostream>

int main()
{
    // create MediaLibrary object
    MediaLibrary library(4);

    // create Media objects in constructor and add to array
    library.addMedia(new Media("Legend", "Daim Bin Khalid"));
    library.addMedia(new Audio("The Sandman", "Neil Gaiman", 320));
    library.addMedia(new Video("The Flash", "DC", "1920x1080"));
    library.addMedia(new Text("Boohoo", "Random Author", 3500));

    std::cout << "Displaying Media Library:" << std::endl;
    library.displayLibrary(); // polymorphic behaviour

    return 0;
}
