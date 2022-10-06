# NFT ART GENERATOR
This tool generates generative NFT art, based of all available traits.  
It was made with the intention to make the generative art field more accessible to anyone.  
With this tool you don't need to be a programmer to create generative art.

**Features:**
* Generate Images of an infinite amount of traits
* Weight traits for different rarities
* Remove duplicated combinations
* Generate metadata for direct use on OpenSea

**Installation**
`npm install -g nft-art-generator`

**Usage**
`nft-generate [--save-config] [--load-config filename]` 

Options
  - save-config: saves all entered values to a config.json file, which gets used in future runs
  - load-config: loads values from a specific json config file

**Documentation**  

Before you start, make sure your file structure looks something like this:

```
YOUR_PROJECT/  
├─ images/  
│  ├─ trait1_name/  
│  │  ├─ file1.png  
│  │  ├─ file2.png  
│  │  ├─ file3.png  
│  │  ├─ ...  
│  ├─ trait2_name/  
│  │  ├─ file4.png  
│  │  ├─ file5.png  
│  │  ├─ ...  
│  ├─ trait3_name/  
│  │  ├─ file6.png  
│  │  ├─ ...  
│  ├─ ...  
```

This is really important, since the scripts imports the traits based on the folder structure.
 
The first input allows you to select where your images are located.  
* Current directory: Will look for an images folder inside the directory the script has been run in.    
* Somewhere else on my computer: Will let you enter an absolute filepath to your images folder.
  
In the next step you are able to select where your files should be outputted to.
* Current directory: Will create a folder called output inside the current location and output all images there.
* Somewhere else on my computer: Will let you enter an absolute filepath to your preferred output folder.  

The next input lets you decide if you want to allow duplicates or not.   

The next input lets you decide if you want to generate metadata or not.

If you want metadata to be generated the script will ask you for a name, a description and an image url.
* Name: Enter the name you want to be saved in the metadata.  
  Example: If you enter Crypto Punk, the script would output Crypto Punk#ID to the metadata


* Description: The description that should be saved in the metadata.


* Image URL: Enter the base url of your images.  
  Example: If you enter https://google.com/api/cryptopunks/, the script will output https://google.com/api/cryptopunks/ID

After that the script will output a list of all traits it could find, and asks you to select your background trait.  
When you did this the script, will continue to ask you which trait should be the next layer.  
Imagine it like the different layers in Photoshop and you are selecting the order of those.

The next input lets you decide if you want to use filenames as traits names, or to define custom names for each trait.  

If you selected the last option, you will enter a name for all your files.   
These names will be used in the Metadata as well as in the script to make weighting the traits easier.  
Example: If you have a file name bg1.png the script will ask you to name it. If its just a white background you could name it "White".

The next step is the weighting of your traits.  
You can enter the amount you want to have of the listed trait.  
Please make sure that all traits end up with the same amount of images, otherwise there will be issues.  
Example: You want 50 total images. You enter 50 White background, 25 red balls and 25 blue balls.  
That would result in 50 total spheres and 50 total background.

Please note that if you selected the option to remove duplicates there might be less images then expected.  

That's it check your output folder for your images and metadata file.

If you encounter any issues feel free to sent me a DM on my Twitter [@notluksus3D](https://twitter.com/notluksus3D)

**Known issues**
Some special characters may resolve in some "File couldnt be loaded" errors.
Try to remove any special characters from your file paths to resolve.
