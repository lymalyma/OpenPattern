# OpenPattern

-----------

OpenPattern is a python library consisting of a set of classes designed to draft 1:1 scale bespoke sewing patterns and save them as pdf (or matplotlib compatible) files for printing or further processing.

Printing can be performed at fullscale on a tracer but OpenPattern can also cut the pattern in as many pieces as needed in order to print them on an A4 printer at home.

OpenPattern can be used to draft patterns from scratch but also includes a set of predefined patterns from bases such as bodices to more elaborate patterns such as shirts.
The patterns are drafted following instructions from three main stylists: <a href="https://lespressesdumidi.com/content/18-jacqueline-chiappetta">Jacqueline Chiappetta</a>, <a href="https://www.editions-eyrolles.com/Auteur/86662/teresa-gilewska">Theresa Gilewska</a> and <a href="https://www.euromodeschool.it/index.html">Antonnio Donnano </a>.  Sizes are stored in a sqlite3 database. By default they include a series of standard (French and Italian) sizes for Women, Men, Girls and Boys given by these authors.

## Installation and Requirements <a class="anchor" id="installation-and-requirements"></a>

### Requirements
OpenPattern requires Python 3.10+ and the following libraries:
* matplotlib
* numpy
* scipy

### Quick Start (Recommended)

Using [uv](https://github.com/astral-sh/uv) (fast, modern Python package manager):

```bash
# Install uv if you haven't
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and install
git clone https://github.com/fmetivier/OpenPattern.git
cd OpenPattern
uv sync
```

### Alternative: pip

```bash
git clone https://github.com/fmetivier/OpenPattern.git
cd OpenPattern
pip install -e .
```

### Development Setup

```bash
uv sync --extra dev    # Install with dev dependencies
uv run pytest          # Run tests
uv run ruff check .    # Lint code
```

### Database Permissions

OpenPattern comes with an sqlite3 `measurements.db` database containing standard French and Italian sizes.
To add your own measurements, you may need to change its permissions:

```bash
# Location varies by installation method
chmod 666 path/to/OpenPattern/data/measurements.db
```


## Example <a class="anchor" id="example"></a>

The most simple way to use OpenPattern is to take advantage one of its predefined patterns. In the example script we plot the bodice  of a women size 36 (French) with bust and waist darts.

```python
import matplotlib.pyplot as plt
import OpenPattern as OP


# Create instance of base class
p = OP.Basic_Bodice(pname = "W36G", gender = 'w', style = 'Gilewska')

# Add darts
p.add_bust_dart()
p.add_waist_dart()

# Call the draw method
p.draw({"Pattern":"Bodice with darts"},save=True)

# Look at the result
plt.show()
```
The result looks like
![Result](./samplePatterns/Gilewska_Basic_Bodice_W36G_FullSize.svg)

## Documentation <a class="anchor" id="documentation"></a>
for more informations on the use of the library see the <a target="_blank" href="https://openpattern.readthedocs.io/en/latest/index.html">Documentation on read the docs</a>.

For an introduction in French see [OpenPattern_F.md](./fdocs/OpenPattern_F.md) in the fdoc section.

typical samples of scripts and patterns can be found in the sampleScripts and samplePatterns section in the docs.
