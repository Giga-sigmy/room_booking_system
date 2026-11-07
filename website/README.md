# Website service description

## Export statics
- Since deploying to github pages requires exporting statics following config was added

```json
    output: 'export', 
    basePath: process.env.PAGES_BASE_PATH,
```
- in case of any issues please report to devops team instead of changing :D
- Please note that this will prevent some of juicy functions like SPA from functioning
## Views
- Main page - Jaś
- Listing all rooms - Monika
- Layout of the floor for booking the room - Jaś
- User profile (user data, user reservations) - Monika
- Login - Monika

## Components
- Header (Logo on the left, login/user description on the right)
- Footer (App name, Authors, UJ data)
- Room booking calendar
- Cancel reservation

