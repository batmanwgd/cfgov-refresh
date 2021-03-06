# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-16 12:41
from __future__ import unicode_literals

import ask_cfpb.models.pages
from django.db import migrations, models
import django.db.models.deletion
import v1.atomic_elements.organisms
import v1.blocks
import wagtail.contrib.wagtailroutablepage.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    replaces = [
        ('regulations3k', '0002_rename_cfr_title'),
        ('regulations3k', '0003_alter_regulationpage_header'),
        ('regulations3k', '0004_add_acquired_and_draft_to_effectiveversion'),
        ('regulations3k', '0005_add_sortable_label_subpart_type'),
        ('regulations3k', '0006_set_sortable_label_subpart_type'),
        ('regulations3k', '0007_make_sortable_label_required'),
        ('regulations3k', '0008_regulationssearchpage'),
        ('regulations3k', '0009_sectionparagraph'),
        ('regulations3k', '0010_rename_acquired_field'),
        ('regulations3k', '0011_add_header_content_to_regs_landing_page'),
        ('regulations3k', '0012_add_regulation_page_content_organisms'),
        ('regulations3k', '0013_add_image_to_fullwidthtext'),
        ('regulations3k', '0014_rm_imageinset_and_media_from_fullwidthtext'),
        ('regulations3k', '0015_rename_regpage_part_related_field'),
        ('regulations3k', '0016_require_effective_date'),
        ('regulations3k', '0017_set_default_created_date'),
        ('regulations3k', '0018_add_notification_block'),
        ('regulations3k', '0019_add_disclaimer_pagechooserblock_to_emailsignup'),
        ('regulations3k', '0020_rm_formfieldwithbutton'),
        ('regulations3k', '0021_rm_hero_links'),
        ('regulations3k', '0022_update_help_cf_link'),
        ('regulations3k', '0023_update_hero_labels_and_help_text'),
        ('regulations3k', '0024_add_standard_notification_regs_landing'),
        ('regulations3k', '0025_part_short_name'),
        ('regulations3k', '0026_migrate_letter_code_to_short_name'),
        ('regulations3k', '0027_remove_part_letter_code'),
        ('regulations3k', '0028_add_ask_search')
    ]

    dependencies = [
        ('v1', '0198_recreated'),
        ('regulations3k', '0029_recreated'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegulationLandingPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
                ('header', wagtail.wagtailcore.fields.StreamField((('hero', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(help_text='For complete guidelines on creating heroes, visit our <a href="https://cfpb.github.io/design-manual/global-elements/heroes.html">Design Manual</a>.<ul class="help">Character counts (including spaces) at largest breakpoint:<li>&bull; 41 characters max (one-line heading)</li><li>&bull; 82 characters max (two-line heading)</li></ul>', required=False)), ('body', wagtail.wagtailcore.blocks.RichTextBlock(help_text='<ul class="help">Character counts (including spaces) at largest breakpoint:<li>&bull; 165-186 characters (after a one-line heading)</li><li>&bull; 108-124 characters (after a two-line heading)</li></ul>', label='Sub-heading', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='When saving illustrations, use a transparent background. <a href="https://cfpb.github.io/design-manual/global-elements/heroes.html#style">See image dimension guidelines.</a>', label='Large image', required=False)), ('small_image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text='<b>Optional.</b> Provides an alternate image for small displays when using a photo or bleeding hero. Not required for the standard illustration. <a href="https://cfpb.github.io/design-manual/global-elements/heroes.html#style">See image dimension guidelines.</a>', required=False)), ('background_color', wagtail.wagtailcore.blocks.CharBlock(help_text='Specify a hex value (with the # sign) from our <a href="https://cfpb.github.io/design-manual/brand-guidelines/color-principles.html">official color palette</a>.', required=False)), ('is_overlay', wagtail.wagtailcore.blocks.BooleanBlock(help_text='<b>Optional.</b> Uses the large image as a background under the entire hero, creating the "Photo" style of hero (see <a href="https://cfpb.github.io/design-manual/global-elements/heroes.html">Design Manual</a> for details). When using this option, make sure to specify a background color (above) for the left/right margins that appear when screens are wider than 1200px and for the text section when the photo and text stack at mobile sizes.', label='Photo', required=False)), ('is_white_text', wagtail.wagtailcore.blocks.BooleanBlock(help_text='<b>Optional.</b> Turns the hero text white. Useful if using a dark background color or background image.', label='White text', required=False)), ('is_bleeding', wagtail.wagtailcore.blocks.BooleanBlock(help_text='<b>Optional.</b> Select if you want the illustration to bleed vertically off the top and bottom of the hero space.', label='Bleed', required=False))))),), blank=True)),
                ('content', wagtail.wagtailcore.fields.StreamField((('notification', wagtail.wagtailcore.blocks.StructBlock((('message', wagtail.wagtailcore.blocks.CharBlock(help_text='The main notification message to display.', required=True)), ('explanation', wagtail.wagtailcore.blocks.TextBlock(help_text='Explanation text appears below the message in smaller type.', required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)))), help_text='Links appear on their own lines below the explanation.', required=False))))), ('full_width_text', wagtail.wagtailcore.blocks.StreamBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.wagtailcore.blocks.StructBlock((('content_block', wagtail.wagtailcore.blocks.RichTextBlock()), ('anchor_link', wagtail.wagtailcore.blocks.StructBlock((('link_id', wagtail.wagtailcore.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False)),)))))), ('heading', wagtail.wagtailcore.blocks.StructBlock((('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))), required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailcore.blocks.StructBlock((('upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.wagtailcore.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))))), ('image_width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('full', 'full'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.wagtailcore.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', wagtail.wagtailcore.blocks.StructBlock((('body', wagtail.wagtailcore.blocks.TextBlock()), ('citation', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('is_large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('cta', wagtail.wagtailcore.blocks.StructBlock((('slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('button', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')])))))))), ('related_links', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False))))))))), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', wagtail.wagtailcore.blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))))), ('well', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(label='Well', required=False)),))), ('well_with_ask_search', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(label='Well', required=False)), ('ask_search', wagtail.wagtailcore.blocks.StructBlock((('show_label', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='Whether to show form label.', required=False)), ('placeholder', wagtail.wagtailcore.blocks.TextBlock(help_text='Text to show for the input placeholder text.', required=False)))))))), ('regulations_list', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(help_text='Regulations list heading', required=False)), ('more_regs_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Link to more regulations')), ('more_regs_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Text to show on link to more regulations', required=False))))))))), blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'v1.cfgovpage'),
        ),
        migrations.CreateModel(
            name='RegulationPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
                ('header', wagtail.wagtailcore.fields.StreamField((('text_introduction', wagtail.wagtailcore.blocks.StructBlock((('eyebrow', wagtail.wagtailcore.blocks.CharBlock(help_text='Optional: Adds an H5 eyebrow above H1 heading text. Only use in conjunction with heading.', label='Pre-heading', required=False)), ('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)))), required=False)), ('has_rule', wagtail.wagtailcore.blocks.BooleanBlock(help_text='Check this to add a horizontal rule line to bottom of text introduction.', label='Has bottom rule', required=False))))),), blank=True)),
                ('content', wagtail.wagtailcore.fields.StreamField((('info_unit_group', wagtail.wagtailcore.blocks.StructBlock((('format', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('50-50', '50/50'), ('33-33-33', '33/33/33'), ('25-75', '25/75')], help_text='Choose the number and width of info unit columns.', label='Format')), ('heading', wagtail.wagtailcore.blocks.StructBlock((('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))), required=False)), ('intro', wagtail.wagtailcore.blocks.RichTextBlock(help_text='If this field is not empty, the Heading field must also be set.', required=False)), ('link_image_and_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text="Check this to link all images and headings to the URL of the first link in their unit's list, if there is a link.", required=False)), ('has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Check this to add a horizontal rule line to top of info unit group.', required=False)), ('lines_between_items', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Check this to show horizontal rule lines between info units.', label='Show rule lines between items', required=False)), ('info_units', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailcore.blocks.StructBlock((('upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.wagtailcore.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))))), ('heading', wagtail.wagtailcore.blocks.StructBlock((('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))), default={'level': 'h3'}, required=False)), ('body', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)))), required=False)))))), ('sharing', wagtail.wagtailcore.blocks.StructBlock((('shareable', wagtail.wagtailcore.blocks.BooleanBlock(help_text='If checked, share links will be included below the items.', label='Include sharing links?', required=False)), ('share_blurb', wagtail.wagtailcore.blocks.CharBlock(help_text='Sets the tweet text, email subject line, and LinkedIn post text.', required=False)))))))), ('full_width_text', wagtail.wagtailcore.blocks.StreamBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(icon='edit')), ('content_with_anchor', wagtail.wagtailcore.blocks.StructBlock((('content_block', wagtail.wagtailcore.blocks.RichTextBlock()), ('anchor_link', wagtail.wagtailcore.blocks.StructBlock((('link_id', wagtail.wagtailcore.blocks.CharBlock(help_text='\n            ID will be auto-generated on save.\n            However, you may enter some human-friendly text that\n            will be incorporated to make it easier to read.\n        ', label='ID for this content block', required=False)),)))))), ('heading', wagtail.wagtailcore.blocks.StructBlock((('text', v1.blocks.HeadingTextBlock(required=False)), ('level', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')])), ('icon', v1.blocks.HeadingIconBlock(help_text='Input the name of an icon to appear to the left of the heading. E.g., approved, help-round, etc. <a href="https://cfpb.github.io/capital-framework/components/cf-icons/#the-icons">See full list of icons</a>', required=False))), required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailcore.blocks.StructBlock((('upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alt', wagtail.wagtailcore.blocks.CharBlock(help_text="If the image is decorative (i.e., if a screenreader wouldn't have anything useful to say about it), leave the Alt field blank.", required=False))))), ('image_width', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('full', 'full'), (470, '470px'), (270, '270px'), (170, '170px')])), ('image_position', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('right', 'right'), ('left', 'left')], help_text='Does not apply if the image is full-width')), ('text', wagtail.wagtailcore.blocks.RichTextBlock(label='Caption', required=False)), ('is_bottom_rule', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='Check to add a horizontal rule line to bottom of inset.', label='Has bottom rule line', required=False))))), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('quote', wagtail.wagtailcore.blocks.StructBlock((('body', wagtail.wagtailcore.blocks.TextBlock()), ('citation', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('is_large', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('cta', wagtail.wagtailcore.blocks.StructBlock((('slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('button', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('large', 'Large Primary')])))))))), ('related_links', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('url', wagtail.wagtailcore.blocks.CharBlock(default='/', required=False))))))))), ('reusable_text', v1.blocks.ReusableTextChooserBlock('v1.ReusableText')), ('email_signup', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(default='Stay informed', required=False)), ('default_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label='Default heading style', required=False)), ('text', wagtail.wagtailcore.blocks.CharBlock(help_text='Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), ('gd_code', wagtail.wagtailcore.blocks.CharBlock(help_text='Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label='GovDelivery code', required=False)), ('disclaimer_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text='Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label='Privacy Act statement', required=False))))), ('well', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(label='Well', required=False)),))), ('well_with_ask_search', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.RichTextBlock(label='Well', required=False)), ('ask_search', wagtail.wagtailcore.blocks.StructBlock((('show_label', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text='Whether to show form label.', required=False)), ('placeholder', wagtail.wagtailcore.blocks.TextBlock(help_text='Text to show for the input placeholder text.', required=False)))))))))))), blank=True, null=True)),
                ('secondary_nav_exclude_sibling_pages', models.BooleanField(default=False)),
                ('regulation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='page', to='regulations3k.Part')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, ask_cfpb.models.pages.SecondaryNavigationJSMixin, 'v1.cfgovpage'),
        ),
        migrations.CreateModel(
            name='RegulationsSearchPage',
            fields=[
                ('cfgovpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.CFGOVPage')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'v1.cfgovpage'),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('contents', models.TextField(blank=True)),
                ('sortable_label', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['sortable_label'],
            },
        ),
        migrations.CreateModel(
            name='SectionParagraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField(blank=True)),
                ('paragraph_id', models.CharField(blank=True, max_length=255)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='regulations3k.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Subpart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('subpart_type', models.IntegerField(choices=[(0, 'Regulation Body'), (1000, 'Appendix'), (2000, 'Interpretation')], default=0)),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subparts', to='regulations3k.EffectiveVersion')),
            ],
            options={
                'ordering': ['subpart_type', 'label'],
            },
        ),
        migrations.AddField(
            model_name='section',
            name='subpart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='regulations3k.Subpart'),
        ),
        migrations.AddField(
            model_name='effectiveversion',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='regulations3k.Part'),
        ),
    ]
