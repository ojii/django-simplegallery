# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Gallery_groups'
        db.create_table('simplegallery_gallery_groups', (
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Gallery_groups+', to=orm['auth.Group'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Gallery_groups+', to=orm['simplegallery.Gallery'])),
        ))
        db.send_create_signal('simplegallery', ['Gallery_groups'])

        # Deleting field 'gallerytranslation.language_id'
        db.delete_column('simplegallery_gallery_translation', 'language_id')

        # Adding field 'GalleryTranslation.language_code'
        db.add_column('simplegallery_gallery_translation', 'language_code', self.gf('django.db.models.fields.CharField')(db_index=True, default='en', max_length=15, blank=True))

        # Removing unique constraint on 'gallerytranslation', fields ['master', 'language_id']
        db.delete_unique('simplegallery_gallery_translation', ['master_id', 'language_id'])

        # Adding unique constraint on 'GalleryTranslation', fields ['master', 'language_code']
        db.create_unique('simplegallery_gallery_translation', ['master_id', 'language_code'])

        # Adding M2M table for field groups on 'Gallery'
        db.create_table('simplegallery_gallery_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm['simplegallery.gallery'], null=False)),
            ('group', models.ForeignKey(orm['auth.group'], null=False))
        ))
        db.create_unique('simplegallery_gallery_groups', ['gallery_id', 'group_id'])

        # Deleting field 'imagetranslation.language_id'
        db.delete_column('simplegallery_image_translation', 'language_id')

        # Adding field 'ImageTranslation.language_code'
        db.add_column('simplegallery_image_translation', 'language_code', self.gf('django.db.models.fields.CharField')(db_index=True, default='en', max_length=15, blank=True))

        # Removing unique constraint on 'imagetranslation', fields ['master', 'language_id']
        db.delete_unique('simplegallery_image_translation', ['master_id', 'language_id'])

        # Adding unique constraint on 'ImageTranslation', fields ['master', 'language_code']
        db.create_unique('simplegallery_image_translation', ['master_id', 'language_code'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Gallery_groups'
        db.delete_table('simplegallery_gallery_groups')

        # Adding field 'gallerytranslation.language_id'
        db.add_column('simplegallery_gallery_translation', 'language_id', self.gf('django.db.models.fields.IntegerField')(default=1, db_index=True))

        # Deleting field 'GalleryTranslation.language_code'
        db.delete_column('simplegallery_gallery_translation', 'language_code')

        # Adding unique constraint on 'gallerytranslation', fields ['master', 'language_id']
        db.create_unique('simplegallery_gallery_translation', ['master_id', 'language_id'])

        # Removing unique constraint on 'GalleryTranslation', fields ['master', 'language_code']
        db.delete_unique('simplegallery_gallery_translation', ['master_id', 'language_code'])

        # Removing M2M table for field groups on 'Gallery'
        db.delete_table('simplegallery_gallery_groups')

        # Adding field 'imagetranslation.language_id'
        db.add_column('simplegallery_image_translation', 'language_id', self.gf('django.db.models.fields.IntegerField')(default=1, db_index=True))

        # Deleting field 'ImageTranslation.language_code'
        db.delete_column('simplegallery_image_translation', 'language_code')

        # Adding unique constraint on 'imagetranslation', fields ['master', 'language_id']
        db.create_unique('simplegallery_image_translation', ['master_id', 'language_id'])

        # Removing unique constraint on 'ImageTranslation', fields ['master', 'language_code']
        db.delete_unique('simplegallery_image_translation', ['master_id', 'language_code'])
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.group_permissions': {
            'Meta': {'unique_together': "(('group', 'permission'),)", 'object_name': 'Group_permissions'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Group_permissions+'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Group_permissions+'", 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'auth.user_groups': {
            'Meta': {'unique_together': "(('user', 'group'),)", 'object_name': 'User_groups'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'User_groups+'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'User_groups+'", 'to': "orm['auth.User']"})
        },
        'auth.user_user_permissions': {
            'Meta': {'unique_together': "(('user', 'permission'),)", 'object_name': 'User_user_permissions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'User_user_permissions+'", 'to': "orm['auth.Permission']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'User_user_permissions+'", 'to': "orm['auth.User']"})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.page': {
            'Meta': {'object_name': 'Page'},
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'menu_login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'moderator_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '1', 'blank': 'True'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True', 'blank': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_file_type_plugin_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': "orm['auth.User']"}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'simplegallery.carouselfeature': {
            'Meta': {'object_name': 'CarouselFeature', 'db_table': "'cmsplugin_carouselfeature'", '_ormbases': ['cms.CMSPlugin']},
            'aspect_ratio': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'interval': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'simplegallery.carouselimage': {
            'Meta': {'object_name': 'CarouselImage'},
            'carousel_feature': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['simplegallery.CarouselFeature']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']"}),
            'ordering': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'title_2': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'simplegallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'simplegallery.gallery_groups': {
            'Meta': {'unique_together': "(('gallery', 'group'),)", 'object_name': 'Gallery_groups'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Gallery_groups+'", 'to': "orm['simplegallery.Gallery']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Gallery_groups+'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'simplegallery.gallerypublication': {
            'Meta': {'object_name': 'GalleryPublication', 'db_table': "'cmsplugin_gallerypublication'", '_ormbases': ['cms.CMSPlugin']},
            'aspect_ratio': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simplegallery.Gallery']"}),
            'interval': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'simplegallery.gallerytranslation': {
            'Meta': {'unique_together': "(('language_code', 'master'),)", 'object_name': 'GalleryTranslation', 'db_table': "'simplegallery_gallery_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['simplegallery.Gallery']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'simplegallery.image': {
            'Meta': {'object_name': 'Image'},
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['simplegallery.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']"}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']", 'null': 'True', 'blank': 'True'})
        },
        'simplegallery.imagetranslation': {
            'Meta': {'unique_together': "(('language_code', 'master'),)", 'object_name': 'ImageTranslation', 'db_table': "'simplegallery_image_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['simplegallery.Image']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['simplegallery']