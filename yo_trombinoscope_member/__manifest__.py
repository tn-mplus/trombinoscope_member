{
    "name": "Trombinoscope Member",
    "version": "18.0.1.0.0",
    "depends": ["web_editor", "membership", "website"],
    "author": "Yotech",
    "license": "Other proprietary",
    "category": "theme",
    "description": """
This module add trombinoscope snippet for odoo Website.
Features including:
- [ID-296-4503/4504] custom trombinoscope member
    """,
    "data": [
        "security/ir.model.access.csv",
        "data/image_library.xml",
        "views/trombinoscope_list.xml",
        'views/snippets/s_trombinoscope_member.xml',
        'views/snippets/snippets.xml',
    ],
    "assets": {
        "website.assets_wysiwyg": [
            "yo_trombinoscope_member/static/src/snippets/s_trombinoscope_member/options.js",
        ],
        "web.assets_frontend": [
            "yo_trombinoscope_member/static/src/snippets/s_trombinoscope_member/000.js",
            "yo_trombinoscope_member/static/src/snippets/s_trombinoscope_member/000.scss",
        ],
    },
}
