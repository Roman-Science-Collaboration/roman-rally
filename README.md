# Roman Rally

Website for **Roman Rally**, hackathon-style working meetings on commissioning and first-look data from NASA's Nancy Grace Roman Space Telescope. The [Roman Science Collaboration](https://outerspace.stsci.edu/spaces/RSCPUB/pages/286851875/Roman+Science+Collaboration+RSC+Public+Page+Home) organizes the series.

The site is a [Jekyll](https://jekyllrb.com/) project so it can be hosted on [GitHub Pages](https://pages.github.com/). Almost every sentence a reader sees is a Markdown file. Collaborators can edit those files in the GitHub website, without installing anything.

The published site, once Pages is turned on, will be:

**https://roman-science-collaboration.github.io/roman-rally/**

Unset facts are written as `**TBD**` (bold TBD on the site). Search the repository for `**TBD**` before announcing a meeting.

## Edit a page in the browser

1. Open the repository on GitHub: [Roman-Science-Collaboration/roman-rally](https://github.com/Roman-Science-Collaboration/roman-rally).
2. Find the file. The usual pages are in the repository root:

   | Page | File |
   | --- | --- |
   | Home | `index.md` |
   | About and philosophy | `about.md` |
   | Events list | `events.md` |
   | Participation and FAQ | `participation.md` |
   | Code of conduct | `code-of-conduct.md` |
   | Contact | `contact.md` |
   | A single meeting | `_events/some-name.md` |

3. Click the pencil icon (**Edit this file**). You can also use the **Edit this page** link in the website footer, which opens the same editor on the `main` branch.
4. Change the words. Leave the lines between the first pair of `---` alone unless you mean to change a title or a date. Those lines are the page header (front matter).
5. Click **Commit changes**. People with write access may commit straight to `main`. Prefer **Create a new branch** and a pull request so someone else can read the edit before it goes live.
6. After the pull request is merged, GitHub Actions rebuilds the site. Give it a minute, then reload the page.

A pull request is the right place for wording. It is the wrong place for a complaint about a person. Conduct reports go to the address on the contact page (still **TBD**), not to a public issue.

## Add an event

Each meeting is one Markdown file in `_events/`. The home page and the events list read those files. You do not edit the list by hand.

1. Open [`_events/TEMPLATE.md`](_events/TEMPLATE.md) and click **Raw**. Select all of the text and copy it.
2. Back in the repository, choose **Add file → Create new file**.
3. Name the file `_events/short-name.md`. Use lowercase letters, numbers, and hyphens, for example `_events/2027-baltimore.md`.
4. Paste the template into the editor.
5. Delete the line `published: false`. While that line is present, Jekyll hides the page.
6. Fill in the header. Quoted `"**TBD**"` values are what the sidebar and the event cards display. Replace each one, and keep the quotes.
7. Set `status` to `upcoming` or `past`.
8. Set `sort_date` to the first day, written `YYYY-MM-DD`, so the list sorts in time. Undated drafts can keep `9999-12-31`, which sorts last.
9. Write the page under the second `---` line. Keep the practical list in the body in step with the header. Both are shown: the header feeds the sidebar and the cards, and the body is the prose.
10. Committee entries are one person per line: `"Name, Institution"`. Replace the `"**TBD**"` line rather than adding names under it.
11. Leave `application_url` as `"**TBD**"` until you have a real `https://` link. A link is rendered as "Application form".
12. Choose **Commit changes → Create a new branch**, then open a pull request.

`_events/TEMPLATE.md` itself stays unpublished. Do not turn it into a real event. Copy it.

To retire a meeting, set `status: past` and add a short note about what people worked on. The events page has a **Past events** section for that list. It is empty until the first Rally is over.

## Preview locally

You need Ruby 3.2 or newer and [Bundler](https://bundler.io/). On Ubuntu, `ruby-full` and `build-essential` are enough. On macOS, Homebrew's `ruby` is a straightforward choice.

```bash
bundle install
bundle exec jekyll serve
```

The first `bundle install` downloads the GitHub Pages gem set. It is slow once, then quick.

Open [http://127.0.0.1:4000/roman-rally/](http://127.0.0.1:4000/roman-rally/). The `/roman-rally` part matches the project-site address. Jekyll rebuilds when you save a file. Stop the server with Ctrl-C.

To build without starting a server:

```bash
bundle exec jekyll build
```

The HTML lands in `_site/`, which is git-ignored. Do not commit it.

## Publish on GitHub Pages

This repository includes a workflow, [`.github/workflows/pages.yml`](.github/workflows/pages.yml). It builds the site with the same `Gemfile` on every pull request. On a push to `main`, it also deploys to GitHub Pages.

An organization owner or a repository admin has to point Pages at that workflow once:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions** (not "Deploy from a branch").
3. Merge a commit to `main`, or run the **Pages** workflow from the Actions tab.
4. When the deploy job is green, the site is at `https://roman-science-collaboration.github.io/roman-rally/`.

Until step 2 is done, the deploy job fails because the `github-pages` environment does not exist yet. The build job can still pass. That first failure is the setting, not a broken site.

If the organization restricts Pages, an owner may also need to allow Pages for this repository under the organization's settings.

Use one publisher. If Source is **GitHub Actions**, do not also turn on **Deploy from a branch**. Two publishers will overwrite each other.

The branch method is a fallback if Actions is unavailable: **Settings → Pages → Deploy from a branch → `main` → `/ (root)`**. GitHub will run its own Jekyll build. In that case, delete or disable `.github/workflows/pages.yml` so the Actions deploy does not also run. The `baseurl` in `_config.yml` can stay `/roman-rally`.

## Add collaborators or a team

The repository belongs to the **Roman-Science-Collaboration** organization. Write access is how someone gets the pencil icon.

**A team (preferred when several people at once should edit):**

1. An organization owner opens the organization on GitHub, then **Teams → New team**. A name such as `rally-editors` is enough.
2. Add people to the team. They need GitHub accounts.
3. On the team's **Repositories** tab, add `roman-rally` with the role **Write**.
4. Members can commit and open pull requests. Give **Maintain** or **Admin** only to people who should change settings, Pages, or access.

**One person:**

1. Open this repository's **Settings → Collaborators and teams** (wording varies: **Collaborators**, or **Manage access**).
2. Add their GitHub username with the role **Write**.

People without write access can still propose an edit. On the file, choose **Edit**, and GitHub will offer a fork and a pull request. That path is fine for a wording change from outside the organization.

## Placeholders

Search the repository for `**TBD**`. Those strings are the facts still missing: dates, venue, host, committees, application, funding, logistics, contact addresses, and a few policy links. The same marker is bold on the website.

`_events/TEMPLATE.md` contains `**TBD**` on purpose. It is a blank form, not a list of missing facts for the first Rally. The first Rally's own file is `_events/first-rally.md`.

## Repository map

```
_config.yml                 site title, URL, and the events collection
_events/                    one Markdown file per meeting
_events/TEMPLATE.md         copy this to add a meeting (stays unpublished)
_layouts/                   HTML shells
_includes/                  header, footer, event cards
assets/css/style.css        layout and color
assets/favicon.svg          icon
assets/wordmark.svg         standalone wordmark
assets/fonts/               Source Serif 4 and Source Sans 3 (SIL Open Font License)
.github/workflows/pages.yml build and deploy
```

The header wordmark is CSS plus a small inline SVG (a milestone on two road lines). Please do not add the NASA insignia, the Roman mission logo, or other agency marks. This is a community site.

Colors and type live in `assets/css/style.css`. Favor the limestone background and the terracotta accent already there.

## License of the fonts

Source Serif 4 and Source Sans 3 are used under the SIL Open Font License. The license texts are `assets/fonts/OFL-source-serif.txt` and `assets/fonts/OFL-source-sans.txt`.
