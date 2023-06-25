#include "media.h"
#include <iostream>

int main()
{
    // create objects of each class
    Media media("Legend", "Daim Bin Khalid");
    Audio audio("The Sandman", "Neil Gaiman", 320);
    Video video("The Flash", "DC", "1920x1080");
    Text text("Boohoo", "Random Author", 3500);

    // call display functions
    media.displayInfo();
    std::cout << std::endl;

    audio.displayAudioInfo();
    std::cout << std::endl;

    video.displayVideoInfo();
    std::cout << std::endl;

    text.displayTextInfo();
    std::cout << std::endl;
}
