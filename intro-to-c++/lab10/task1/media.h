#ifndef MEDIA_H // wrapper to handle multiple header import errors
#define MEDIA_H

#include <string>
using std::string;

// define classes
class Media
{
private:
    string title;
    string author;

public:
    // constructor
    Media(const string &title, const string &author);

    void displayInfo();

    // getter functions
    string getTitle();
    string getAuthor();
};

class Audio : public Media
{
private:
    int audio_quality;

public:
    // constructor
    Audio(const string &title, const string &author, int audio_quality);

    void displayAudioInfo();
    int getAudioQuality();
};

class Video : public Media
{
private:
    string resolution;

public:
    // constructor
    Video(const string &title, const string &author, string resolution);

    void displayVideoInfo();
    string getResolution();
};

class Text : public Media
{
private:
    int numOfWords;

public:
    // constructor
    Text(const string &title, const string &author, int numOfWords);

    void displayTextInfo();
    int getNumOfWords();
};

#endif
