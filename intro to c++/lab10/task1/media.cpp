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

int Audio::getAudioQuality()
{
    return this->audio_quality;
}

void Audio::displayAudioInfo()
{
    this->displayInfo();
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

void Video::displayVideoInfo()
{
    this->displayInfo();
    cout << "Resolution: " << this->getResolution() << " pixels" << endl;
}

// define Text class
Text::Text(const string &title, const string &author, int numOfWords_input)
    : Media(title, author) // base class constructor
{
    this->numOfWords = numOfWords_input;
}

int Text::getNumOfWords()
{
    return this->numOfWords;
}

void Text::displayTextInfo()
{
    this->displayInfo();
    cout << "Number of Words: " << this->getNumOfWords() << endl;
}
