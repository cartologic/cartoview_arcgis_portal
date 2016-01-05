# Cartoview ArcGIS Portal

Portal for ArcGIS Implementaation using dajngo. The app is integrated with [cartoview](https://github.com/cartologic/cartoview) to manage maps and layers with the use of [Cartoview arcgis feature server](https://github.com/cartologic/cartoview_arcgis_feature_server).

# Installation

1. Install [Cartoview arcgis feature server](https://github.com/cartologic/cartoview_arcgis_feature_server).
2. Download the app package form [here](http://cartologic.com/cartoview2/apps/)
3. in your [cartoview](github.com/cartologic/cartoview) installation, login as admin
4. go to "Apps" then "Manage Apps" then "Install new app"
5. upload the downloaded package and click install
6. wait untill the installation finish
7. (NOTE) there is a bug in cartoview which prevent the app to be installed correctely. untail we fix this bug please do the following steps
8. open command line then navigate to geonode folder using the command ```cd "C:\Program Files (x86)\Geonode\geonode"```
9. activate the geonode virtual environment by running the batch file ```"C:\Program Files (x86)\Geonode\env_geonode\Scripts\activate.bat"```
10. run the command ```python manage.py syncdb```

# Support
for now the portal is supporting web maps only

# License
BSD2

Copyright (c) 2015, Cartologic.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. All advertising materials mentioning features or use of this software must display the following acknowledgement: This product includes software developed by the Cartologic.
4. Neither the name of the Cartologic nor the names of its contributors may be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY CARTOLOGIC ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL CARTOLOGIC BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
