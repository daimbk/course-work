#include "media.h"
#include <iostream>

using std::cout, std::endl;

// define Media class
// constructor
Media::Media(const string &title_input, const string &author_input)
{
    this->title = title_input;
    this->author = author_input;
}

// destructor
Media::~Media()
{
}

// define functionality for friend functions
string Media::getTitle()
{
    return this->title;
}

string Media::getAuthor()
{
    return this->author;
}

void Media::displayInfo()
{
    cout << "Title: " << this->getTitle() << endl;
    cout << "Author: " << this->getAuthor() << endl;
}

// define Audio class
Audio::Audio(const string &title, const string &author, int audio_quality_input)
    : Media(title, author) // base class constructor
{
    this->audio_quality = audio_quality_input;
}

Audio::~Audio()
{
}

int Audio::getAudioQuality()
{
    return this->audio_quality;
}

void Audio::displayInfo()
{
    Media::displayInfo(); // call parent function
    cout << "Quality: " << this->getAudioQuality() << " Kbps" << endl;
}

// define Video class
Video::Video(const string &title, const string &author, string resolution_input)
    : Media(title, author)
{
    this->resolution = resolution_input;
}

string Video::getResolution()
{
    return this->resolution;
}

void Video::displayInfo()
{
    Media::displayInfo();
    cout << "Resolution: " << this->getResolution() << " pixels" << endl;
}

// define Text class
Text::Text(const string &title, const string &author, int numOfWords_input)
    : Media(title, author) // base class constructor
{
    this->numOfWords = numOfWords_input;
}

Text::~Text()
{
}

int Text::getNumOfWords()
{
    return this->numOfWords;
}

void Text::displayInfo()
{
    Media::displayInfo();
    cout << "Number of Words: " << this->getNumOfWords() << endl;
}

// define MediaLibrary class
MediaLibrary::MediaLibrary(int size_input)
{
    this->size = size_input;
    this->iterator = 0;
    this->mediaArray = new Media *[size]; // create dynamic array
}

// define destructor to delete pointers in array
MediaLibrary::~MediaLibrary()
{
    // delete object pointers in
    // loop till iterator to avoid empty array elements
    for (int i = 0; i < this->iterator; i++)
    {
        delete mediaArray[i];
    }

    // delete array
    delete[] mediaArray;
}

void MediaLibrary::addMedia(Media *media_obj)
{
    if (iterator < size)
    {
        mediaArray[iterator] = media_obj;
        iterator++; // increment to next empty element
    }
    else
    {
        cout << "Cannot add more as library is full" << endl;
    }
}

void MediaLibrary::displayLibrary()
{
    for (int i = 0; i < iterator; ++i)
    {
        mediaArray[i]->displayInfo(); // each object will call its own displayInfo
        cout << endl;
    }
}
