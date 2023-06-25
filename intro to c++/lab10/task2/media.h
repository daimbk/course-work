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

    // destructor
    virtual ~Media();

    virtual void displayInfo(); // make virtual for dynamic binding

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

    // destructor
    ~Audio();

    void displayInfo() override; // override for polymorphism
    int getAudioQuality();
};

class Video : public Media
{
private:
    string resolution;

public:
    // constructor
    Video(const string &title, const string &author, string resolution);

    void displayInfo() override;
    string getResolution();
};

class Text : public Media
{
private:
    int numOfWords;

public:
    // constructor
    Text(const string &title, const string &author, int numOfWords);

    // destructor
    ~Text();

    void displayInfo() override;
    int getNumOfWords();
};

// MediaLibrary class
class MediaLibrary
{
private:
    Media **mediaArray; // dynamic array of Media object for polymorphism
    int size;
    int iterator;

public:
    // constructor
    MediaLibrary(int capacity);

    // destructor
    ~MediaLibrary();

    void addMedia(Media *media_obj);
    void displayLibrary();
};

#endif
