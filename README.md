# CodeSignal Developer Docs

A place to put documentation about interacting with our APIs.

## Running locally
You can view the documentation site locally by running `npm start` -- you just need to have Python 3 installed on your local machine.
The start script serves the docs here: http://localhost:8000

Since it's a static site, you can also just open `/docs/index.html` directly in a web browser if you prefer.

## Modifying the event diagrams

The diagrams are generated using the following tool [diagrams](https://app.diagrams.net).

1. Go to that specific URL.
2. Open existing diagram.
3. Open `docs/diagrams/webhooks-flow.drawio` file.
4. Make all the needed changes.
  * Note that the document has 2 pages -- one with the entire flow and one with individual sections.
5. Save the changes and put the resulting file on the repository to overwrite `docs/diagrams/webhooks-flow.drawio` file.

To update each image:

1. Select everything you'd like to export. 
2. Click on File -> Export -> PNG.
3. Make sure 'Selection Only' checkbox is checked.
4. Overwrite the existing images with the new ones.

## Generating GraphQL docs
GraphQL API docs are generated with graphqldoc:
https://github.com/codesignal/graphqldoc

To generate documentation:
- The default endpoint is set to [http://app.codesignal.com/graphql](https://app.codesignal.com/graphql), so ensure that latest version is deployed already.
- Check out this repository and run `npm install`, then `npm run build`.
- Static pages will be generated under `/docs/graphql/types`.
- Make sure they look okay, then commit and push.
 
## How to publish updated docs
This repo is hosted with GitHub Pages, so any change under `/docs` on the `master` branch will be published here:
https://codesignal.github.io/developer-docs/
Which in return should be redirected to this subdomain: developer.codesignal.com

That's it! You should see your changes there once they reach the master branch, as long as they are under `/docs`. 

Don't change the GraphQL `/docs/types/` pages manually, since your changes will be overwritten the next time those pages are generated.
It's okay to change other pages manually.
