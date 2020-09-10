## Dynamic.py

Python script that strips unnecessary files from a ReactJs production build App and
renames random generated names of static files to more Dynamics friendly filenames,
ready to be uploaded as Dynamics 365 web resources.

#### REQUIREMENTS:
    Python 3.8+

#### USAGE:
 - build your react app with `npm run build`
 - place `dynamic.py` in the same directory as the `build` directory.
 - run `dynamic.py` by locating the dynamic.py directory in cmd
 - run command: `python dynamic.py`.

#### NOTES:
 - the **index.html** should remain as `index.html` before running **dynamic.py**, you can rename it afterwards
 - the unnecessary files will be stored in the `extras` directory
 - all remaining files in the build directory should be uploaded to Dynamics as **web resources**
 - web resource example url: `/WebResources/<SOLUTION_NAME>_react/static/js/2.chunk.js`
 - web resource example url: `/WebResources/<SOLUTION_NAME>_react/index.html`
