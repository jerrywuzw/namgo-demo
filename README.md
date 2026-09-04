# NAMGO — demo site

Clickable prototype of the NAMGO platform, built for partner and shop-owner
conversations. Single self-contained `index.html`, no build step, no dependencies.

**Live:** https://jerrywuzw.github.io/namgo-demo/

## What's in it

Four screens, switched from the top nav:

| Screen | What it shows |
|---|---|
| **Home** | Animated landing page with a **working earnings calculator** |
| **Storefront** | `namgo.com/dao-artisan-noodle` — real SKUs, prices, per-item delivery dates, working cart |
| **Dashboard** | Sales, units, royalties, traffic by channel, compare-to-similar-shops |
| **Design Studio** | Upload a real logo and watch it land on the product mockups |

## The calculator

The landing page calculator is live, not a mockup. It runs the funnel model
from playbook §6:

- Counter QR converts ~1.5% of monthly foot traffic into storefront visits
- Instagram drives ~1% of followers as clicks per month
- Visits convert to orders at 5% (warm affinity traffic, vs. 1.4–2.7% typical ecommerce)
- AOV fixed at $38

Every one of those is a **planning assumption**, printed on the page under the
result. They get replaced with measured actuals after day 30/60 of launch.

## Demo notes

- Best moment on a call is the **Design Studio** — upload the owner's actual
  logo while they watch.
- All figures shown are planning assumptions pending confirmed factory quotes,
  customs classification, and fulfillment contracts. Nothing here is a commitment.
- The card art on the home screen is a CSS gradient placeholder. Swapping in a
  real Dao Artisan Noodle photo would meaningfully sharpen it.

## Pages

`index.html` is the source of truth. The two comparison pages are generated
copies of it, each with its own view active and its own title, description and
canonical URL:

| URL | File |
|---|---|
| `/` | `index.html` |
| `/vs-printful/` | `vs-printful/index.html` |
| `/vs-clover/` | `vs-clover/index.html` |

Regenerate them after editing `index.html`:

```bash
python3 build-pages.py
```

They are copies rather than hand-written pages so the styling can never drift.
Do not edit anything under `vs-printful/` or `vs-clover/` directly — it will be
overwritten on the next run.

## Local preview

Open `index.html` in a browser, or:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

## Editing

Everything lives in `index.html` — tokens at the top of the `<style>` block
control the whole palette:

```css
--ground: #f2eedc;  /* cream page */
--ink:    #57181f;  /* oxblood display type + accent */
```

Dark mode is defined alongside it and follows the viewer's system setting.
