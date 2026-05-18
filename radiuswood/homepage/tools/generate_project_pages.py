#!/usr/bin/env python3
"""Generate the 8 project pages in /work/ using the new theme + shared site.css."""
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work"

# All 8 projects in the requested feature order.
PROJECTS = [
    {
        "slug": "vancouverhouse-bop-penthouse",
        "title_html": "Vancouverhouse <em>BOP Penthouse</em>",
        "title_text": "Vancouverhouse BOP Penthouse",
        "breadcrumb": "Vancouverhouse BOP Penthouse",
        "award_strip": "Inside Bjarke Ingels Group's Vancouver House",
        "meta_desc": "The BOP penthouse inside BIG's Vancouver House. Bookmatched walnut slat ceilings, three-storey Bocci pendant stairwell, curved walnut slat wall in the master ensuite. Photography Kent Leckie 2020.",
        "hero_img": "../projects/vancouverhouse-bop-penthouse.jpg",
        "hero_caption": "Living room facing the atrium garden · Walnut slat ceiling · Photography Kent Leckie 2020",
        "schema_locality": "Vancouver",
        "schema_street": "1480 Howe Street",
        "schema_year": "2020",
        "schema_desc": "Penthouse interior inside Bjarke Ingels Group's Vancouver House tower. Walnut slat ceilings + walls, walnut bookmatched cabinetry, black marble counters, Bocci pendant stairwell, curved walnut slat wall in the master ensuite.",
        "meta_cells": [
            ("Building", "Vancouver House,<br>1480 Howe Street"),
            ("Tower Architect", "Bjarke Ingels<br>Group (BIG)"),
            ("Year", "2020"),
            ("Photography", "Kent Leckie"),
            ("Lead Species", "American walnut,<br>bookmatched"),
            ("Standout", "Bocci pendant<br>stairwell"),
        ],
        "brief": [
            "A penthouse inside <strong>Bjarke Ingels Group's Vancouver House</strong> — the twisting triangle tower at the south edge of downtown Vancouver. The shell is iconic; the interior had to live up to it without competing with it. The brief landed on a single material gesture: <strong>American walnut, bookmatched, run as both ceiling slats and full-height cabinetry</strong>, with black marble as the counter-note and Bocci as the lighting move.",
            "The standout is the stairwell. A <strong>three-storey Bocci 28 pendant installation</strong> fills the central void, visible from inside the apartment through a glass wall and from the street at dusk. The stair itself is bookmatched walnut and blackened steel, treads cantilevered off the side wall.",
        ],
        "work": [
            "The walnut slat ceilings are the thing you remember. <strong>One-inch-wide bookmatched walnut strips on five-inch centres</strong>, run continuously across the kitchen, dining, and living plates. Each strip is veneer over a Baltic-birch core; the bookmatch holds across every panel break so the figure travels uninterrupted across the whole apartment ceiling.",
            "The kitchen is dark and quiet. <strong>Black marble counters and backsplash</strong>, integrated black handles, bookmatched walnut on every door and drawer face. The hood is hidden inside the walnut soffit — no metal, no visible mechanism. Open shelving in the same walnut, marble shelves at the back wall, a single column of glass-fronted display behind the cooktop.",
            "The master ensuite is the project's flex move. <strong>A curved walnut slat wall</strong> wraps the freestanding tub — same one-inch slats as the ceiling, but tilted to a continuously varying radius. Each slat was cut as its own ribbon and set against a curved spine; the spine is bent-laminated walnut around a steel substructure.",
        ],
        "gallery_1": (
            ("../photos/vancouverhouse-bop-penthouse/vancouverhouse-bop-penthouse-kitchen-walnut-marble-backsplash-island.jpg", "Kitchen with bookmatched walnut, black marble backsplash, walnut slat ceiling overhead"),
            ("../photos/vancouverhouse-bop-penthouse/vancouverhouse-bop-penthouse-bocci-stairwell-dusk-exterior-view.jpg", "Three-storey Bocci pendant installation in the stairwell, dusk exterior view"),
            ("../photos/vancouverhouse-bop-penthouse/vancouverhouse-bop-penthouse-walnut-slat-corridor-bocci-stair-view.jpg", "Walnut slat corridor with view to Bocci stairwell installation through doorway"),
        ),
        "spec": [
            ("Ceiling + Walls", "Bookmatched American walnut · 1″ slats on 5″ centres"),
            ("Kitchen Cabinetry", "Bookmatched walnut · integrated black handles · concealed hood"),
            ("Counters", "Black marble · waterfall edge · matching backsplash"),
            ("Master Ensuite", "Curved walnut slat wall · bent-laminated spine on steel"),
            ("Powder Bath", "Stone trough sink · mirror-wall vanity · walnut bases"),
            ("Stair", "Cantilevered bookmatched walnut treads · blackened steel"),
            ("Lighting", "Bocci 28 series · three-storey stairwell cluster"),
            ("Finish", "Hard-wax oil · matte sheen · open grain"),
        ],
        "gallery_2": (
            ("../photos/vancouverhouse-bop-penthouse/vancouverhouse-bop-penthouse-master-bath-freestanding-tub-curved-walnut-slat-wall.jpg", "Master ensuite with freestanding tub against a curved walnut slat wall"),
            ("../photos/vancouverhouse-bop-penthouse/vancouverhouse-bop-penthouse-powder-bath-trough-sink-mirror-wall.jpg", "Powder bath with stone trough sink, mirror-wall vanity, walnut detailing"),
            ("../photos/vancouverhouse-bop-penthouse/vancouverhouse-bop-penthouse-kitchen-walnut-hood-open-shelving-pantry.jpg", "Kitchen with walnut concealed hood, open shelving, pantry"),
        ),
        "quote": "One-inch walnut slats on five-inch centres, run continuously across the ceiling and around the curve of the tub wall. The bookmatch holds across every break. The figure travels.",
        "related": ["indian-river-the-point", "waterfront-anigre-penthouse", "indian-arm-study"],
    },
    {
        "slug": "indian-arm-study",
        "title_html": "Indian Arm <em>Study</em>",
        "title_text": "Indian Arm Study",
        "breadcrumb": "Indian Arm Study",
        "award_strip": "",
        "meta_desc": "Cedar-lined writer's cabin on Indian Arm. Stone fireplace wall, globe-pendant cluster, built-in cedar bookcase + desk, ocean view through full-height glazing.",
        "hero_img": "../projects/indian-arm-study.jpg",
        "hero_caption": "Living room — cedar ceiling, stone wall, globe pendant cluster, ocean view",
        "schema_locality": "North Vancouver",
        "schema_street": "Indian Arm",
        "schema_year": "",
        "schema_desc": "Cedar-lined writer's cabin on Indian Arm. Stone wall feature, globe-pendant cluster, built-in cedar bookcase + ocean-view desk niche.",
        "meta_cells": [
            ("Location", "Indian Arm,<br>North Vancouver BC"),
            ("Setting", "Waterfront,<br>writer's cabin"),
            ("Scope", "Whole-cabin<br>millwork"),
            ("Lead Species", "Cedar +<br>local stone"),
            ("Standout", "Stone +<br>cedar feature wall"),
            ("Furniture", "Curved-edge<br>desk niche"),
        ],
        "brief": [
            "A writer's cabin on Indian Arm. <strong>Cedar tongue-and-groove</strong> for the ceiling, walls, and the built-in bookcase that lines one whole side of the room. A wall of <strong>locally collected stone</strong> as the counter-note — dry-stacked, no mortar joint visible from the room side.",
            "The brief was to keep the room quiet. Cedar's golden warmth balances the cool grey of the stone. The view through the full-height glazing is the only artwork the room needs.",
        ],
        "work": [
            "The cedar runs in continuous courses from one end of the cabin to the other. Tongue-and-groove edges, set with the figure aligned across every plane break — wall into ceiling, ceiling into return. Where the cedar meets the stone wall, the joint is a hairline reveal scribed to the stone profile.",
            "The <strong>built-in desk</strong> is a single curved-edge slab cantilevered off the cedar wall. No leg, no support visible — the structure runs back into the wall. Above the desk, a vertical bookcase with adjustable shelves; below, drawers for paper, ink, and the things that gather on a writer's desk.",
            "A <strong>globe pendant cluster</strong> on a red-cable harness drops from the cedar ceiling — Bocci-style, but in a tighter cluster. The leather Maralunga is the only piece of furniture in the room that isn't built in.",
        ],
        "gallery_1": (
            ("../photos/indian-arm-study/indian-arm-woodlands-study-living-room-wide-cedar-ceiling.jpg", "Living room wide — cedar ceiling and stone wall with globe pendant cluster"),
            ("../photos/indian-arm-study/indian-arm-woodlands-study-cedar-bookcase-pink-chair-sailboat.jpg", "Cedar built-in bookcase with pink chair and sailboat model in window"),
            ("../photos/indian-arm-study/indian-arm-woodlands-study-cedar-desk-curved-edge-ocean-view.jpg", "Cedar built-in desk with curved edge and ocean view"),
        ),
        "spec": [
            ("Walls + Ceiling", "Western red cedar · tongue-and-groove, slip-matched"),
            ("Feature Wall", "Locally collected stone · dry-stacked"),
            ("Bookcase", "Cedar built-in · full-height, adjustable shelves"),
            ("Desk", "Curved-edge slab · cantilevered, no visible support"),
            ("Pendants", "Globe cluster on red-cable harness"),
            ("Glazing", "Full-height ocean-view window wall"),
            ("Finish", "Hard-wax oil · cedar"),
            ("Floor", "Wide-plank white oak · matte"),
        ],
        "gallery_2": (
            ("../photos/indian-arm-study/indian-arm-woodlands-study-leather-chair-globe-pendants-vertical.jpg", "Leather Maralunga chair with globe pendant cluster against cedar wall"),
            ("../photos/indian-arm-study/indian-arm-woodlands-study-cedar-built-in-stone-fireplace-tight.jpg", "Cedar built-in detail with stone fireplace tight crop"),
            ("../photos/indian-arm-study/indian-arm-woodlands-study-exterior-cedar-cabin-dusk-trees.jpg", "Exterior cedar cabin at dusk among trees"),
        ),
        "quote": "Cedar runs in continuous courses from one end of the cabin to the other. Where it meets the stone, the joint is scribed to the rock — a hairline reveal, no caulk, no margin.",
        "related": ["indian-river-the-point", "vancouverhouse-bop-penthouse", "lions-bay"],
    },
    {
        "slug": "indian-river-the-point",
        "title_html": "Indian River — <em>The Point</em>",
        "title_text": "Indian River — The Point",
        "breadcrumb": "Indian River — The Point",
        "award_strip": "",
        "meta_desc": "Modern gable-end residence on Indian Arm. Slip-matched rift white oak interior throughout. River-rock chimney column. Black wenge dining wall. Bocci pendant cluster. Tongue-and-groove white oak stair. Photography Andrew Latreille.",
        "hero_img": "../projects/indian-river-the-point.jpg",
        "hero_caption": "Living room · Gable-end glazing · Bocci pendant cluster · Slip-matched rift white oak · Photography Andrew Latreille",
        "schema_locality": "North Vancouver",
        "schema_street": "Indian Arm",
        "schema_year": "2025",
        "schema_desc": "Modern gable-end residence on Indian Arm. Slip-matched rift white oak interior throughout. River-rock chimney column. Black wenge dining wall. Tongue-and-groove white oak stair. Bocci pendant cluster over the harbor-view living room.",
        "meta_cells": [
            ("Location", "Indian Arm,<br>North Vancouver BC"),
            ("Year", "2025"),
            ("Photography", "Andrew Latreille"),
            ("Scope", "Whole-house<br>millwork"),
            ("Lead Species", "Slip-matched<br>rift white oak"),
            ("Setting", "Waterfront<br>residence"),
        ],
        "brief": [
            "A gable-end residence on Indian Arm where the architectural move is a single tall window framing the harbor — and the millwork has to hold its own next to it. <strong>Slip-matched rift white oak</strong> through the public rooms, a <strong>river-rock chimney column</strong> rising past the slats, <strong>black wenge</strong> as the dark counter-note in the dining wall, and a tongue-and-groove stair worked in the same oak as the cabinetry so it reads as one continuous material gesture.",
            "The point of slip-matching, plainly, is that the figure runs the room. Every door, every panel, every drawer face is from the same flitch, sequenced in the order the boards came off the log. You stop seeing cabinetry and start seeing the tree.",
        ],
        "work": [
            "Slip-matching at this scale is a logistics problem before it's a craftsmanship problem. The figure has to land where the eye lands — at the door breaks, at the appliance returns, at the line where a wall plane turns into a ceiling soffit. <strong>The flitch gets sequenced on the floor in shop order before it ever sees a press</strong>, and every modification request post-glue-up gets weighed against losing the run.",
            "The <strong>moss-green island</strong> is a counterpoint. Painted, not stained — the saturation needed a paint base. Honed soapstone top, oil rub, a softer hand than granite. The <strong>black wenge dining wall</strong> is the inverse: a dark, dense African hardwood that swallows light. Three black globe pendants, leather chairs, the trio reads as a tonal echo of the wenge.",
            "The stair is <strong>tongue-and-groove white oak</strong>, set into a stack-bond pattern. Same flitch as the kitchen cabinetry. The handrail is a continuous milled section. The vertical pickets are integral, not applied — cut from the same oak and slid into the stringer like a comb.",
        ],
        "gallery_1": (
            ("../photos/indian-river-the-point/indian-river-the-point-kitchen-white-oak-slat-wall-river-rock-fireplace-column.jpg", "Kitchen and dining with floor-to-ceiling white oak slat wall and river-rock chimney column"),
            ("../photos/indian-river-the-point/indian-river-the-point-dining-black-wenge-cabinets-pendant-trio-leather-chairs.jpg", "Dining with black wenge buffet wall, trio of black globe pendants, leather chairs"),
            ("../photos/indian-river-the-point/indian-river-the-point-kitchen-white-oak-pantry-open-moss-green-island.jpg", "White oak coffee/breakfast pantry, doors open, moss-green island corner"),
        ),
        "spec": [
            ("Primary Species", "Rift white oak · slip-matched flitch"),
            ("Counter-Note", "Black wenge · solid stock for dining wall"),
            ("Island", "Painted moss-green · honed soapstone top"),
            ("Stair", "Tongue-and-groove rift white oak · integral pickets"),
            ("Chimney", "Field-collected river rock · dry-stacked"),
            ("Master Wardrobe", "Slip-matched rift oak · full-height door wall"),
            ("Ensuite Vanity", "Rift oak base · honed limestone · sage tile field"),
            ("Joinery", "Slip-matched veneer · integral handles · tongue-and-groove"),
            ("Finish", "Hard-wax oil · matte sheen"),
        ],
        "gallery_2": (
            ("../photos/indian-river-the-point/indian-river-the-point-master-bedroom-white-oak-wardrobe-wall.jpg", "Master bedroom with full-height slip-matched rift oak wardrobe wall"),
            ("../photos/indian-river-the-point/indian-river-the-point-master-ensuite-rift-oak-vanity-freestanding-tub-green-tile.jpg", "Master ensuite with rift oak vanity, freestanding tub, sage-green tile field"),
            ("../photos/indian-river-the-point/indian-river-the-point-white-oak-stair-tongue-and-groove.jpg", "Tongue-and-groove rift white oak stair with integral pickets"),
        ),
        "quote": "The point of slip-matching is that the figure runs the room. Every door, every panel from the same flitch, in the order the boards came off the log. You stop seeing cabinetry and start seeing the tree.",
        "related": ["vancouverhouse-bop-penthouse", "indian-arm-study", "waterfront-anigre-penthouse"],
    },
    {
        "slug": "west-vancouver-modern-luxury",
        "title_html": "West Vancouver <em>Modern Luxury</em>",
        "title_text": "West Vancouver Modern Luxury",
        "breadcrumb": "West Vancouver Modern Luxury",
        "award_strip": "",
        "meta_desc": "Modern coastal residence in West Vancouver. Banded cedar-slat ceiling lights, saffron-uppered coffee bar, concrete columns, glass curtain walls, pool deck at dusk. Wine cellar with antique carved doors.",
        "hero_img": "../projects/west-vancouver-modern-luxury.jpg",
        "hero_caption": "Coffee bar — banded cedar-slat ceiling lights, glass sliders, ocean-view deck",
        "schema_locality": "West Vancouver",
        "schema_street": "",
        "schema_year": "",
        "schema_desc": "Modern coastal residence in West Vancouver. Banded cedar-slat ceiling lights, saffron-uppered coffee bar, concrete columns, glass curtain walls. Wine cellar with antique carved doors.",
        "meta_cells": [
            ("Location", "West Vancouver,<br>BC"),
            ("Setting", "Coastal modern,<br>ocean view"),
            ("Scope", "Whole-house<br>millwork"),
            ("Lead Species", "Cedar +<br>oak built-ins"),
            ("Standout", "Banded slat<br>ceiling lights"),
            ("Feature", "Wine cellar with<br>antique carved doors"),
        ],
        "brief": [
            "A modern coastal residence in West Vancouver with the kind of view that the architecture is built to frame. <strong>Cedar-slat ceiling bands</strong> with integrated downlight strips run across the main public rooms — a ceiling that's also the lighting plan. Glass curtain walls slide open to a cantilevered ocean-view deck.",
            "The interior's signature counter-note is a pair of <strong>antique carved double doors</strong> sourced from an estate sale, restored and re-hung as the entry to a wine cellar lined with spiral racking. The contrast — patinated old wood against the clean modern shell — is the whole project's argument.",
        ],
        "work": [
            "The ceiling is the project's central craft problem. <strong>Cedar slats set in continuous bands</strong>, with the downlights threaded through the gap between slats — no visible fixture, no surface cans, just the wood and the light. Each band runs the full length of the room; the joint where the band breaks is hidden in shadow.",
            "The kitchen and coffee bar share the same vocabulary: <strong>saffron-painted upper cabinets</strong>, grey textured base cabinets, AEG appliances. The colour reads warm against the cedar without competing with it. The cooktop wall is white-oak slat — a continuation of the ceiling band, turned vertical.",
            "The <strong>wine cellar entry</strong> is where the project earns its keep. Antique double doors, hand-carved with iron grille work, set into a clean white-oak frame. Inside the cellar: spiral bottle racks rising the full height of the room, lit from below for the wine-bottle wall.",
        ],
        "gallery_1": (
            ("../photos/west-vancouver-modern-luxury/west-vancouver-modern-luxury-coffee-bar-ceiling-banded-lights-fireplace-wide.jpg", "Coffee bar wide with banded cedar-slat ceiling lights, fireplace, glass sliders"),
            ("../photos/west-vancouver-modern-luxury/west-vancouver-modern-luxury-coffee-bar-saffron-uppers-grey-textured.jpg", "Coffee bar with saffron uppers, grey textured bases, AEG oven"),
            ("../photos/west-vancouver-modern-luxury/west-vancouver-modern-luxury-wine-cellar-antique-carved-doors-interior-view.jpg", "Wine cellar interior view through antique carved doors"),
        ),
        "spec": [
            ("Ceiling", "Cedar slats · continuous bands · integrated downlights"),
            ("Kitchen Cabinetry", "Saffron-painted uppers · grey textured bases · AEG appliances"),
            ("Coffee Bar", "Light wood + saffron storage wall"),
            ("Wine Cellar Doors", "Antique hand-carved double doors · iron grille work · restored"),
            ("Wine Cellar Interior", "Spiral bottle racks · full-height · backlit display"),
            ("Stair", "Curved · concrete wall · cherry-wood treads"),
            ("Ensuite", "Concrete-look vanity · shower w/ handheld + body sprays"),
            ("Exterior", "Ipe-deck cantilever · cedar railing · pool integration"),
            ("Finish", "Cedar oil · oak hardwax · concrete sealer"),
        ],
        "gallery_2": (
            ("../photos/west-vancouver-modern-luxury/west-vancouver-modern-luxury-curved-stair-concrete-wall-cherry-treads.jpg", "Curved stair with concrete wall and cherry-wood treads"),
            ("../photos/west-vancouver-modern-luxury/west-vancouver-modern-luxury-kitchen-saffron-storage-wall-light-wood.jpg", "Kitchen saffron storage wall with light wood detail"),
            ("../photos/west-vancouver-modern-luxury/west-vancouver-modern-luxury-exterior-deck-pool-ocean-view-cedar-railing.jpg", "Exterior deck with pool, ocean view, cedar railing"),
        ),
        "quote": "Cedar slats in continuous bands, downlights threaded through the gap. No fixtures, no cans — just the wood and the light.",
        "related": ["lions-bay", "indian-river-the-point", "indian-arm-study"],
    },
    {
        "slug": "waterfront-anigre-penthouse",
        "title_html": "Waterfront <em>Anigre Penthouse</em>",
        "title_text": "Waterfront Anigre Penthouse",
        "breadcrumb": "Waterfront Anigre Penthouse",
        "award_strip": "",
        "meta_desc": "Harbor-front penthouse with diamond-bookmatched anigre ceiling running through the public rooms. Gallery wine bar with Inuit sculpture collection. Bocci pendant cluster. Travertine + anigre art-deco stair. Hempenstall photography.",
        "hero_img": "../projects/waterfront-anigre-penthouse.jpg",
        "hero_caption": "Living-dining at dusk · Diamond-bookmatched anigre ceiling · Stone fireplace · Gallery wine bar · Photography Hempenstall",
        "schema_locality": "Vancouver",
        "schema_street": "",
        "schema_year": "",
        "schema_desc": "Harbor-front penthouse with diamond-bookmatched anigre ceiling, anigre cabinetry, Bocci pendant cluster, travertine art-deco stair, gallery wine bar with Inuit sculpture collection, rooftop terrace with sauna and ipe slat screens.",
        "meta_cells": [
            ("Location", "Vancouver waterfront,<br>BC"),
            ("Photography", "Hempenstall"),
            ("Lead Species", "Anigre &amp;<br>American walnut"),
            ("Scope", "Whole-penthouse<br>millwork"),
            ("Standout", "Diamond-bookmatched<br>ceiling"),
            ("Lighting", "Bocci pendant<br>cluster"),
        ],
        "brief": [
            "A harbor-front penthouse where the ceiling does the heavy lifting. <strong>Diamond-bookmatched anigre panels</strong> over a steel armature, sequenced so that every diamond rotates the flitch ninety degrees — the figure of the wood reads as a single woven plane from any vantage in the room. Beneath it, a <strong>Bocci pendant cluster</strong>, a granite-topped kitchen island, and a gallery wine bar built around the owner's collection of Inuit soapstone sculpture.",
            "The brief asked the millwork to act like architecture. Not cabinetry serving a room — cabinetry <em>defining</em> the room. Every plane is anigre, every line aligns, and the lit display niches across the back wall are part of the same wood gesture as the panel walls and the ceiling.",
        ],
        "work": [
            "The ceiling came first. <strong>Anigre</strong> — a West African hardwood with a long, satin figure — was selected for the way its grain catches raking light. The diamonds are <strong>four-flitch bookmatch on a 45-degree grid</strong>, each panel CNC-routed to a tolerance that lets the ninety-degree grain rotations meet without a visible seam. The substrate is a Baltic-birch ply spine; the show face is 0.6mm veneer over an MDO core for dimensional stability.",
            "The wine bar is its own room within the room. <strong>Lit anigre display niches</strong> step across the back wall behind tempered glass; the bottle racks pull out as a single carriage so the cellar drops into the millwork instead of hanging off it. The pull-out liquor cabinet — full-height anigre door, opens to reveal racked bottles — disappears entirely when closed.",
            "The <strong>art-deco stair</strong> at the entry is a counter-gesture. Travertine treads, LED-lit risers, and an <strong>open anigre shelving wall</strong> that wraps the stair on the inside line. Maritime artifacts in the niches — sextants, telescopes, a polished brass diving helmet — the curated edit reads as a private museum the moment you step in.",
        ],
        "gallery_1": (
            ("../photos/waterfront-anigre-penthouse/waterfront-anigre-penthouse-kitchen-bocci-pendants-granite-island-anigre-cabinetry.jpg", "Kitchen with Bocci pendant cluster, granite island, anigre cabinetry"),
            ("../photos/waterfront-anigre-penthouse/waterfront-anigre-penthouse-gallery-wine-bar-anigre-display-inuit-sculpture.jpg", "Gallery wine bar with anigre cabinetry, Inuit soapstone sculptures"),
            ("../photos/waterfront-anigre-penthouse/waterfront-anigre-penthouse-dining-bocci-glass-table-sectional-harbor-view-diamond-ceiling.jpg", "Dining area with Bocci cluster, glass table, harbor view, diamond ceiling overhead"),
        ),
        "spec": [
            ("Ceiling", "Diamond-bookmatched anigre · 45° grid · four-flitch rotation"),
            ("Walls + Cabinetry", "Slip-matched anigre · same flitch family as ceiling"),
            ("Kitchen Counter", "Honed granite · waterfall edge"),
            ("Wine Bar", "Anigre w/ lit niches · tempered glass · pull-out liquor carriage"),
            ("Stair", "Travertine treads · LED-lit risers · open anigre shelving wall"),
            ("Ensuite Vanity", "Travertine top + base · anigre drawer faces · teak tub headrest"),
            ("Lighting", "Bocci 28 series · single-source cluster over dining"),
            ("Substrate", "Baltic-birch ply spine · MDO core for show-face panels"),
            ("Finish", "Conversion varnish · satin sheen · between-coat sanded"),
        ],
        "gallery_2": (
            ("../photos/waterfront-anigre-penthouse/waterfront-anigre-penthouse-stair-anigre-shelving-wall-led-step-lights-travertine-treads.jpg", "Art-deco stair with open anigre shelving wall, LED-lit step lights, travertine treads"),
            ("../photos/waterfront-anigre-penthouse/waterfront-anigre-penthouse-media-tv-fireplace-diamond-ceiling-inuit-gallery-wall.jpg", "Media room with TV over stone fireplace, diamond ceiling, Inuit sculpture gallery wall"),
            ("../photos/waterfront-anigre-penthouse/waterfront-anigre-penthouse-master-ensuite-travertine-vanity-tub-shower-wide.jpg", "Master ensuite with travertine vanity, tub, shower"),
        ),
        "quote": "The point of the diamond bookmatch is that it isn't decoration. The grain rotates ninety degrees and back again, and the room reads as one woven plane from anywhere you stand.",
        "related": ["vancouverhouse-bop-penthouse", "indian-river-the-point", "contemporary-walnut-estate"],
    },
    {
        "slug": "lions-bay",
        "title_html": "Lion's Bay <em>Residence</em>",
        "title_text": "Lion's Bay Residence",
        "breadcrumb": "Lion's Bay Residence",
        "award_strip": "",
        "meta_desc": "Oceanfront luxury residence on Howe Sound. Traditional antique-white painted millwork, Viking range kitchen, vaulted ceilings, curved dining nook with bay window framing the islands.",
        "hero_img": "../projects/lions-bay.jpg",
        "hero_caption": "Curved dining nook · Bay-window framing Howe Sound · Painted built-ins · Vaulted ceiling",
        "schema_locality": "Lion's Bay",
        "schema_street": "Howe Sound",
        "schema_year": "",
        "schema_desc": "Oceanfront luxury residence on Howe Sound. Traditional antique-white painted millwork, Viking range kitchen, vaulted ceilings, curved dining nook with bay window.",
        "meta_cells": [
            ("Location", "Lion's Bay,<br>Howe Sound BC"),
            ("Setting", "Oceanfront,<br>island view"),
            ("Scope", "Whole-house<br>millwork"),
            ("Aesthetic", "Traditional<br>antique-white"),
            ("Standout", "Curved dining nook<br>bay window"),
            ("Kitchen", "Viking range,<br>painted cabinetry"),
        ],
        "brief": [
            "A traditional oceanfront residence on Howe Sound with a view of the islands you don't have to be told to look at. <strong>Antique-white painted millwork</strong> throughout — the cabinetry, the panelling, the corbel-carrying mantels, the beadboard inserts. A <strong>red Viking range</strong> as the kitchen's single saturated note.",
            "The architectural move is a <strong>curved dining nook</strong> that wraps the corner of the public room, framing the harbour through a bay window. The built-in millwork carries through the public rooms — TV walls, library-style bookcases, butler's pantry, foyer balcony with iron rail — all in the same painted vocabulary.",
        ],
        "work": [
            "The cabinetry is <strong>antique-white over hard maple</strong>, painted at the shop and finished with a low-VOC conversion varnish that holds up to coastal humidity. The glaze is a single application — wiped, not sprayed — and the resulting figure follows the carved profiles into the corners where painters don't always go.",
            "<strong>Hand-carved corbels</strong> sit under every mantel and counter overhang — turned and carved at the bench, not bought in. Same for the dentil mouldings along the upper cabinetry and the carved-panel inserts on the island corners. The work is fussy by design, finished by hand because the room won't accept anything that looks machine-cut.",
            "The <strong>red Viking range</strong> is the only piece in the kitchen that isn't painted or stained — a deliberate temperature break against the antique-white. The tile mural over the range is hand-painted, commissioned for the house.",
        ],
        "gallery_1": (
            ("../photos/lions-bay/lions-bay-residence-kitchen-wide-antique-white-island-viking-range.jpg", "Kitchen wide with antique-white island and red Viking range"),
            ("../photos/lions-bay/lions-bay-residence-living-room-curved-dining-nook-ocean-view.jpg", "Living room with curved dining nook, bay window, ocean view"),
            ("../photos/lions-bay/lions-bay-residence-kitchen-arched-opening-living-room-wide.jpg", "Kitchen with arched opening to living room, wide perspective"),
        ),
        "spec": [
            ("Cabinetry", "Hard maple · antique-white painted · low-VOC conversion varnish"),
            ("Glaze", "Hand-wiped single-application glaze · follows carved profiles"),
            ("Corbels", "Hand-carved · turned at the bench"),
            ("Mouldings", "Dentil crown · carved-panel inserts · custom profiles"),
            ("Kitchen Range", "Red Viking · single saturated note"),
            ("Tile Mural", "Hand-painted · commissioned for the house"),
            ("Floors", "Wide-plank reclaimed oak · matte"),
            ("Dining Nook", "Curved bay window · built-in banquette · custom radius"),
            ("Finish", "Conversion varnish · between-coat sanded"),
        ],
        "gallery_2": (
            ("../photos/lions-bay/lions-bay-residence-kitchen-viking-range-hood-tile-mural.jpg", "Kitchen Viking range with carved corbels and tile mural"),
            ("../photos/lions-bay/lions-bay-residence-painted-corbel-carved-detail.jpg", "Hand-carved painted corbel close-up detail"),
            ("../photos/lions-bay/lions-bay-residence-glazed-walnut-bar-console-birch-art.jpg", "Glazed walnut bar console with birch art"),
        ),
        "quote": "Antique-white over hard maple, painted at the shop, glazed by hand. The figure follows the carved profiles into the corners where painters don't always go.",
        "related": ["whitby-estates-walnut", "contemporary-walnut-estate", "west-vancouver-modern-luxury"],
    },
    {
        "slug": "contemporary-walnut-estate",
        "title_html": "Contemporary <em>Walnut Estate</em>",
        "title_text": "Contemporary Walnut Estate",
        "breadcrumb": "Contemporary Walnut Estate",
        "award_strip": "",
        "meta_desc": "Vancouver estate with full-house slip-matched American walnut. Dining feature wall with lit fireplace and floor-to-ceiling wine display. Walnut wine cellar with vertical-rod racking. Walnut media room and his/hers walk-ins.",
        "hero_img": "../projects/contemporary-walnut-estate.jpg",
        "hero_caption": "Dining — walnut feature wall, lit fireplace, beach photograph at left, floor-to-ceiling wine display at right",
        "schema_locality": "Vancouver",
        "schema_street": "",
        "schema_year": "",
        "schema_desc": "Vancouver estate with full-house slip-matched American walnut. Dining feature wall with lit fireplace and floor-to-ceiling wine display. Walnut wine cellar with vertical-rod racking.",
        "meta_cells": [
            ("Location", "Vancouver,<br>BC"),
            ("Setting", "Estate residence,<br>contemporary"),
            ("Scope", "Whole-house<br>millwork"),
            ("Lead Species", "Slip-matched<br>American walnut"),
            ("Standout", "Walnut wine cellar<br>+ vertical-rod racks"),
            ("Master Suite", "Walnut wardrobe<br>headboard wall"),
        ],
        "brief": [
            "A Vancouver estate where the brief was a single material gesture: <strong>slip-matched American walnut, run through every public and private room</strong>. The dining feature wall lights a fireplace into the walnut grain. The wine cellar reads as a single sculpted volume of walnut and bottles. The master suite headboard wall continues the same flitch into the bedroom.",
            "The house is contemporary in proportion — high ceilings, clean returns, no applied moulding — but rich in material. The walnut is the project's argument.",
        ],
        "work": [
            "The dining feature wall is the project's anchor. <strong>Walnut panels run from floor to ceiling</strong>, with a stone-surround fireplace inset at the centre. The slip-match holds across the panel returns into the side walls; from the dining table the room reads as a single wrapped envelope of walnut.",
            "The <strong>wine cellar</strong> is the project's deepest craft moment. Walnut wall panelling and walnut bottle racks — <strong>vertical-rod racking</strong> tensioned between the floor and ceiling, with cork-faced bottle cradles. The bottles read as floating against the dark walnut field. The cellar is glass-fronted to the hallway; the racks become the wall.",
            "The <strong>master suite headboard wall</strong> is a full-height walnut panelling treatment that continues the same flitch as the public-room cabinetry. His-and-hers walk-in closets carry the walnut through the dressing room, into custom walnut dressers and shoe walls.",
        ],
        "gallery_1": (
            ("../photos/contemporary-walnut-estate/contemporary-walnut-estate-dining-room-wide-fireplace-wine-wall.jpg", "Dining room wide with walnut feature wall, lit fireplace, wine wall"),
            ("../photos/contemporary-walnut-estate/contemporary-walnut-estate-wine-cellar-walnut-rack-perspective.jpg", "Walnut wine cellar with vertical-rod racks in perspective"),
            ("../photos/contemporary-walnut-estate/contemporary-walnut-estate-master-bedroom-headboard-wall-wide.jpg", "Master bedroom with full-height walnut headboard wall"),
        ),
        "spec": [
            ("Public-Room Cladding", "Slip-matched American walnut · floor-to-ceiling"),
            ("Dining Feature Wall", "Walnut panels w/ stone-surround fireplace inset"),
            ("Wine Cellar", "Walnut panelling + vertical-rod racking · cork bottle cradles"),
            ("Wine Cellar Glazing", "Full-height glass · cellar reads as wall"),
            ("Master Bedroom", "Walnut headboard wall · same flitch as public rooms"),
            ("Walk-In Closets", "Walnut shelving, dressers, shoe walls (his + hers)"),
            ("Media Room", "Walnut TV credenza · backlit panel feature"),
            ("Powder Bath", "Round backlit mirror · stone vanity · walnut detail"),
            ("Finish", "Hard-wax oil · open grain"),
        ],
        "gallery_2": (
            ("../photos/contemporary-walnut-estate/contemporary-walnut-estate-walnut-fireplace-wall-detail.jpg", "Walnut fireplace wall vertical detail with lit fire"),
            ("../photos/contemporary-walnut-estate/contemporary-walnut-estate-wine-cellar-walnut-racks-detail.jpg", "Walnut wine cellar vertical-rod racks detail close-up"),
            ("../photos/contemporary-walnut-estate/contemporary-walnut-estate-media-room-walnut-cabinetry-screen.jpg", "Media room with walnut credenza and projection screen"),
        ),
        "quote": "Slip-matched American walnut, run through every public and private room. The dining wall, the wine cellar, the bedroom — same flitch, one continuous figure.",
        "related": ["whitby-estates-walnut", "waterfront-anigre-penthouse", "vancouverhouse-bop-penthouse"],
    },
    {
        "slug": "whitby-estates-walnut",
        "title_html": "Whitby <em>Estates Walnut</em>",
        "title_text": "Whitby Estates Walnut",
        "breadcrumb": "Whitby Estates Walnut",
        "award_strip": "",
        "meta_desc": "Maghsoud Residence at Whitby Estates. Cherry-walnut media room with coffered ceiling, mahogany double-door entry with crotch-mahogany inlay, travertine floor, ornate hand-carved corbels. Foyer rotunda with saffron dome.",
        "hero_img": "../projects/whitby-estates-walnut.jpg",
        "hero_caption": "Media room corner · Cherry-walnut built-ins · Coffered ceiling · Mahogany double-door entry",
        "schema_locality": "West Vancouver",
        "schema_street": "",
        "schema_year": "",
        "schema_desc": "Maghsoud Residence at Whitby Estates. Cherry-walnut media room with coffered ceiling, mahogany double-door entry with crotch-mahogany inlay, travertine floor, ornate hand-carved corbels.",
        "meta_cells": [
            ("Location", "West Vancouver,<br>Whitby Estates"),
            ("Setting", "Estate residence,<br>traditional"),
            ("Scope", "Whole-house<br>millwork"),
            ("Lead Species", "Cherry +<br>mahogany"),
            ("Standout", "Coffered media<br>room ceiling"),
            ("Feature", "Hand-carved<br>corbels"),
        ],
        "brief": [
            "The Maghsoud Residence at Whitby Estates — a traditional Persian-influenced estate where the millwork vocabulary is <strong>cherry-walnut panelling, coffered ceilings, and hand-carved corbels</strong> over every mantel and counter overhang. The whole-house package included the media room, library, butler's pantry, his-and-hers walk-ins, a foyer rotunda, a wrought-iron stair, and an elevator cab lined in matching cherry.",
            "Every detail is hand-finished. The crown mouldings are dentil-pattern. The mahogany doors carry crotch-mahogany inlay panels. The travertine floors are pattern-cut. The brief was clear: every surface a craftsman would notice.",
        ],
        "work": [
            "The <strong>media room is the project's centrepiece</strong>. Cherry-walnut wall panelling rises to a coffered ceiling — recessed panels in a grid pattern, with dentil-mould crown lining every coffer. Built-in cabinetry wraps the room: TV-over-fireplace centrepiece, glass-front display cabinets at the corners, integrated bar nook.",
            "The <strong>mahogany double doors</strong> at the entry carry <strong>crotch-mahogany inlay panels</strong> — the figured-grain section of the log, sliced for the crown of each panel. Hand-cut, book-matched, set into the door's stile-and-rail frame. Every door in the suite — entry, secondary, wine cellar — uses the same vocabulary.",
            "The <strong>hand-carved corbels</strong> are turned and chiseled at the bench, then finished to match the cherry. Same for the dentil-pattern crowns on the upper cabinetry, the carved panel inserts on the bar nook doors, and the ornate scrollwork on the kitchen-island brackets.",
        ],
        "gallery_1": (
            ("../photos/whitby-estates-walnut/whitby-estates-walnut-maghsoud-residence-media-room-wide-coffered-tv-fireplace-built-ins.jpg", "Media room wide with coffered ceiling, TV over fireplace, full-height built-ins"),
            ("../photos/whitby-estates-walnut/whitby-estates-walnut-maghsoud-residence-mahogany-double-doors-open-entry-perspective.jpg", "Mahogany double doors open with view into media room"),
            ("../photos/whitby-estates-walnut/whitby-estates-walnut-maghsoud-residence-mantel-carved-corbel-close-up.jpg", "Hand-carved cherry corbel close-up under mantel"),
        ),
        "spec": [
            ("Public-Room Panelling", "Cherry-walnut · custom-stained · hand-finished"),
            ("Coffered Ceiling", "Recessed grid panels · dentil-mould crown per coffer"),
            ("Mahogany Doors", "Stile-and-rail w/ crotch-mahogany inlay panels"),
            ("Corbels", "Hand-carved · turned at the bench"),
            ("Mouldings", "Dentil-pattern crown · carved-panel inserts"),
            ("Wine Cellar Door", "Walnut corner glass cabinet · arched niche"),
            ("Elevator Cab", "Cherry-panelled w/ stainless doors"),
            ("Foyer Rotunda", "Saffron-stained dome ceiling"),
            ("Stair", "Wrought-iron · marble medallion floor"),
            ("Floors", "Travertine · pattern-cut"),
            ("Finish", "Conversion varnish · multi-coat · hand-rubbed"),
        ],
        "gallery_2": (
            ("../photos/whitby-estates-walnut/whitby-estates-walnut-maghsoud-residence-cherry-panel-wall-bookmatched-detail.jpg", "Cherry-panel wall vertical detail showing bookmatched figure"),
            ("../photos/whitby-estates-walnut/whitby-estates-walnut-maghsoud-residence-walnut-pantry-glass-cabinets-arched-niche.jpg", "Walnut pantry with glass cabinets and arched niche"),
            ("../photos/whitby-estates-walnut/whitby-estates-walnut-maghsoud-residence-glass-mahogany-double-doors-closed.jpg", "Glass-paneled mahogany double doors closed front view"),
        ),
        "quote": "Crotch-mahogany inlay in every door panel. Hand-cut, book-matched, set into the stile-and-rail. The figured-grain section of the log — sliced for the crown of each panel.",
        "related": ["contemporary-walnut-estate", "lions-bay", "vancouverhouse-bop-penthouse"],
    },
]


SLUG_TO_PROJECT = {p["slug"]: p for p in PROJECTS}


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_text} · Radius Architectural Millwork</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="https://radiuswood.com/our-work/{slug}/">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "{title_text}",
  "creator": {{"@type": "Organization", "name": "Radius Architectural Millwork Ltd"}},
  "locationCreated": {{"@type": "Place", "address": {{"@type": "PostalAddress", "addressLocality": "{schema_locality}", "addressRegion": "BC", "addressCountry": "CA"{street_field}}}}},{date_field}
  "image": "https://radiuswood.com/our-work/{hero_img_rel}",
  "description": "{schema_desc}"
}}
</script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,300;1,400;1,500&family=Roboto:wght@300;400;500&family=Varta:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/site.css">
</head>
<body>

<nav class="site" id="nav">
  <a href="../" class="brand-lockup">
    <img class="logo" src="https://mattanthonyphoto.github.io/matt-proposals/radiuswood/posts/brand/radius-logo.png" alt="Radius Architectural Millwork">
  </a>
  <div class="links">
    <div class="nav-item">
      <a href="../about/">About <span class="caret">▾</span></a>
      <div class="dropdown">
        <a href="../about/company.html">Company</a>
        <a href="../about/our-vision.html">Our Vision</a>
        <a href="../about/partners.html">Partners</a>
      </div>
    </div>
    <div class="nav-item">
      <a href="../services/">Services <span class="caret">▾</span></a>
      <div class="dropdown">
        <a href="../services/architectural-millwork.html">Architectural Millwork</a>
        <a href="../services/3d-renderings.html">3D Renderings</a>
      </div>
    </div>
    <a href="./">Our Work</a>
    <a href="../blog/">Blog</a>
    <a href="../contact.html">Contact</a>
    <a href="../contact.html" class="cta">Get In Touch</a>
  </div>
</nav>

<section class="project-hero">
  <div class="project-hero-inner">
    <span class="eyebrow">Our Work</span>
    {award_strip_block}<h1>{title_html}</h1>
    <div class="breadcrumb">
      <a href="../">Home</a><span class="sep">/</span><a href="./">Our Work</a><span class="sep">/</span><span>{breadcrumb}</span>
    </div>
  </div>
</section>

<div class="project-hero-img">
  <img src="{hero_img}" alt="{title_text} — hero image">
</div>
<div class="project-hero-caption">{hero_caption}</div>

<section class="project-meta-strip">
  <div class="project-meta-grid">
    {meta_cells_html}
  </div>
</section>

<section class="project-section">
  <div class="project-section-inner split-grid">
    <div><span class="eyebrow">The Brief</span></div>
    <div>
      {brief_html}
    </div>
  </div>
</section>

<section class="gallery-1">
  <div class="g-grid">
    <figure><img src="{g1_main_src}" alt="{g1_main_alt}"></figure>
    <div class="stack">
      <figure><img src="{g1_stack1_src}" alt="{g1_stack1_alt}"></figure>
      <figure><img src="{g1_stack2_src}" alt="{g1_stack2_alt}"></figure>
    </div>
  </div>
</section>

<section class="project-section">
  <div class="project-section-inner split-grid">
    <div><span class="eyebrow">The Work</span></div>
    <div>
      {work_html}
    </div>
  </div>
</section>

<section class="spec-block">
  <div class="spec-inner">
    <div>
      <span class="eyebrow">Material Spec</span>
      <h2>The vocabulary, <em>in plain terms.</em></h2>
    </div>
    <div class="spec-table">
      {spec_rows_html}
    </div>
  </div>
</section>

<section class="gallery-2">
  <div class="gallery-2-inner">
    <figure><img src="{g2_1_src}" alt="{g2_1_alt}"></figure>
    <figure><img src="{g2_2_src}" alt="{g2_2_alt}"></figure>
    <figure><img src="{g2_3_src}" alt="{g2_3_alt}"></figure>
  </div>
</section>

<section class="project-quote">
  <div class="project-quote-inner">
    <div class="mark">"</div>
    <blockquote>{quote}</blockquote>
    <cite>Rick Wilson · Owner + Master Joiner</cite>
  </div>
</section>

<section class="related-work">
  <div class="related-head">
    <h2>Related <em>Work</em></h2>
    <a href="./">All Projects →</a>
  </div>
  <div class="related-grid">
    {related_html}
  </div>
</section>

<section class="cta-band">
  <span class="eyebrow">Get in touch</span>
  <h2>Working on a project? <em>Send us the set.</em></h2>
  <p>Drawings, scope, timeline, or just a conversation. We respond within two business days with a feasibility read and a tested quote.</p>
  <a href="../contact.html" class="cta-btn">Request a Quote</a>
</section>

<footer class="site">
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-col footer-brand">
        <img src="https://mattanthonyphoto.github.io/matt-proposals/radiuswood/posts/brand/radius-logo.png" alt="Radius Architectural Millwork">
        <p>A Master Joiner-led custom millwork shop in Burnaby, BC. Twenty-five years on the same bench.</p>
        <div class="legal">Since 2002 · Burnaby BC<br>AWMAC Gold 2011 · 5× Best of Houzz<br>Licence BUS05-01768</div>
      </div>
      <div class="footer-col">
        <h4>About</h4>
        <ul>
          <li><a href="../about/company.html">Company</a></li>
          <li><a href="../about/our-vision.html">Our Vision</a></li>
          <li><a href="../about/partners.html">Partners</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="../services/architectural-millwork.html">Architectural Millwork</a></li>
          <li><a href="../services/3d-renderings.html">3D Renderings</a></li>
          <li><a href="./">Our Work</a></li>
          <li><a href="../blog/">Blog</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Service Area</h4>
        <ul>
          <li>Vancouver</li>
          <li>Burnaby</li>
          <li>West Vancouver</li>
          <li>North Vancouver</li>
          <li>Whistler · Squamish</li>
        </ul>
      </div>
      <div class="footer-col footer-contact">
        <h4>Contact</h4>
        <div class="row"><span class="label">Phone</span><div class="val"><a href="tel:6044441175">604 444 1175</a></div></div>
        <div class="row"><span class="label">Email</span><div class="val"><a href="mailto:rick@radiuswood.com">rick@radiuswood.com</a></div></div>
        <div class="row"><span class="label">Shop</span><div class="val">Unit 106 – 8575<br>Government St, Burnaby</div></div>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© 2026 Radius Architectural Millwork Ltd.</div>
      <div class="socials">
        <a href="https://instagram.com/radiusmillwork" target="_blank" rel="noopener">Instagram</a>
        <a href="https://linkedin.com/company/radius-architectural-millwork" target="_blank" rel="noopener">LinkedIn</a>
        <a href="#" target="_blank" rel="noopener">Houzz</a>
      </div>
    </div>
  </div>
</footer>

<script>
  const nav = document.getElementById('nav');
  document.addEventListener('scroll', () => {{
    nav.classList.toggle('scrolled', window.scrollY > 70);
  }}, {{ passive: true }});
</script>

</body>
</html>
"""


def render_meta_cells(cells):
    rows = []
    for label, value in cells:
        rows.append(f'<div class="cell"><div class="label">{label}</div><div class="value">{value}</div></div>')
    return "\n    ".join(rows)


def render_paragraphs(paragraphs):
    return "\n      ".join(f"<p>{p}</p>" for p in paragraphs)


def render_spec(spec):
    return "\n      ".join(
        f'<div class="spec-row"><div class="key">{key}</div><div class="val">{val}</div></div>'
        for key, val in spec
    )


def render_related(related_slugs, current_slug):
    chunks = []
    for slug in related_slugs:
        if slug == current_slug or slug not in SLUG_TO_PROJECT:
            continue
        p = SLUG_TO_PROJECT[slug]
        chunks.append(textwrap.dedent(f"""
    <a href="{slug}.html" class="related-card">
      <img src="{p['hero_img']}" alt="{p['title_text']}">
      <div class="related-meta">
        <div class="num">{p['meta_cells'][0][1].replace('<br>', ' · ')}</div>
        <h3>{p['title_html']}</h3>
      </div>
    </a>""").strip())
    return "\n    ".join(chunks)


def render_project(project):
    award_strip_block = (
        f'<span class="award-strip">{project["award_strip"]}</span>\n    '
        if project["award_strip"]
        else ""
    )
    street_field = (
        f', "streetAddress": "{project["schema_street"]}"'
        if project["schema_street"]
        else ""
    )
    date_field = (
        f'\n  "dateCreated": "{project["schema_year"]}",'
        if project["schema_year"]
        else ""
    )
    g1_main, g1_stack1, g1_stack2 = project["gallery_1"]
    g2_1, g2_2, g2_3 = project["gallery_2"]

    return PAGE_TEMPLATE.format(
        slug=project["slug"],
        title_html=project["title_html"],
        title_text=project["title_text"],
        breadcrumb=project["breadcrumb"],
        meta_desc=project["meta_desc"],
        hero_img=project["hero_img"],
        hero_img_rel=project["hero_img"].replace("../", ""),
        hero_caption=project["hero_caption"],
        schema_locality=project["schema_locality"],
        schema_desc=project["schema_desc"],
        street_field=street_field,
        date_field=date_field,
        award_strip_block=award_strip_block,
        meta_cells_html=render_meta_cells(project["meta_cells"]),
        brief_html=render_paragraphs(project["brief"]),
        work_html=render_paragraphs(project["work"]),
        g1_main_src=g1_main[0],
        g1_main_alt=g1_main[1],
        g1_stack1_src=g1_stack1[0],
        g1_stack1_alt=g1_stack1[1],
        g1_stack2_src=g1_stack2[0],
        g1_stack2_alt=g1_stack2[1],
        spec_rows_html=render_spec(project["spec"]),
        g2_1_src=g2_1[0],
        g2_1_alt=g2_1[1],
        g2_2_src=g2_2[0],
        g2_2_alt=g2_2[1],
        g2_3_src=g2_3[0],
        g2_3_alt=g2_3[1],
        quote=project["quote"],
        related_html=render_related(project["related"], project["slug"]),
    )


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    for project in PROJECTS:
        out = WORK / f"{project['slug']}.html"
        out.write_text(render_project(project))
        print(f"OK {project['slug']}.html")


if __name__ == "__main__":
    main()
