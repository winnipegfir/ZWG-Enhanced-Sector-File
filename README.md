![Winnipeg FIR](https://winnipegfir.ca/storage/files/uploads/1638293555.png)
<img alt="GitHub all releases" src="https://img.shields.io/github/downloads/winnipegfir/ZWG-Enhanced-Sector-File/total">

## What is it?
The Winnipeg FIR has decided to open-source it's sector-file to allow for contributions from our members! Any aspect of our sector-file (not including NavData) can be changed within this repository and added to our sector file.

### Contributing
#### Pull Requests
We are very interested in having contributions to the sector file. We ask that you consider the following guidelines:

##### Guidelines:
- Use a descriptive but consise title for your PR
- Please be clear with what you have changed or fixed
- Provide screenshots to better describe changes (if possible)
- Be prepared to answer any questions about your PR during review
- Provide references to prove what you've done is correct (if applicable)

#### Issues
We understand that some people don't know how to edit sector files... and that's okay! We ask that you submit an issue through the `Issues` tab on this repository.

**NOTE: It doesn't necessarily have to be an issue, it can also be a suggestion**

##### Guidelines:
- Please be clear with what you are requesting (include screenshots if applicable)
- Please don't spam with unnecessary issues

## First-time Installation Instructions
1. [Download latest release](https://github.com/winnipegfir/ZWG-Enhanced-Sector-File/releases) (any file starting with `CZWG_Full`, .zip file is more common).
2. Unzip the downloaded file. You can store the unzipped folder anywhere on your computer.
3. Open the folder and open `CZWG.prf` with Euroscope.
*Make sure you use `Open with` function on Windows if your computer doesn't launch the file in Euroscope automatically. Do not use the open button in Euroscope to open a .prf file!*
4. Once `CZWG.prf` has opened in Euroscope, you can click `Open SCT` then `Load sector file` to load the .sct file included with the package.

## Auto-installation
The sector file is designed with automatic installation in mind using Euroscope's built-in functionality.

Click `Open SCT` then `Download Sector Files...`, you should see the following when you first install the files.

![Sector File Provider](https://i.imgur.com/K70pZhV.png)

This means that the provider is working properly. You might get asked to load a new sector file when it auto-downloads.

If it isn't working as expected, you can add the provider manually. Ensure you set the URL as `http://files.winnipegfir.ca/` (trailing slash is important). Checking the `A` box on the provider and the provided file is important for getting the files to update automatically.

Previous releases of the sector file will be provided in case of any issues (can be downloaded from the same menu.)
