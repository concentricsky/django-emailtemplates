# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

# Safe User import for Django < 1.5
try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
else:
    User = get_user_model()

# With the default User model these will be 'auth.User' and 'auth.user'
# so instead of using orm['auth.User'] we can use orm[user_orm_label]
user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)
user_model_label = '%s.%s' % (User._meta.app_label, User._meta.module_name)

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RequiredContextItem'
        db.delete_table('emailtemplates_requiredcontextitem')

        # Deleting model 'ModelTemplate'
        db.delete_table('emailtemplates_modeltemplate')

        # Adding field 'EmailTemplate.base_template'
        db.add_column('emailtemplates_emailtemplate', 'base_template',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024, blank=True),
                      keep_default=False)

        # Adding field 'EmailTemplate.body'
        db.add_column('emailtemplates_emailtemplate', 'body',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'RequiredContextItem'
        db.create_table('emailtemplates_requiredcontextitem', (
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(related_name='required_contexts', to=orm['emailtemplates.ModelTemplate'])),
            ('key', self.gf('django.db.models.fields.SlugField')(max_length=64)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='requiredcontextitem_updated', null=True, to=orm[user_orm_label], on_delete=models.SET_NULL, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='requiredcontextitem_created', null=True, to=orm[user_orm_label], on_delete=models.SET_NULL, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('emailtemplates', ['RequiredContextItem'])

        # Adding model 'ModelTemplate'
        db.create_table('emailtemplates_modeltemplate', (
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='modeltemplate_updated', null=True, to=orm[user_orm_label], on_delete=models.SET_NULL, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='modeltemplate_created', null=True, to=orm[user_orm_label], on_delete=models.SET_NULL, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True, blank=True)),
        ))
        db.send_create_signal('emailtemplates', ['ModelTemplate'])

        # Deleting field 'EmailTemplate.base_template'
        db.delete_column('emailtemplates_emailtemplate', 'base_template')

        # Deleting field 'EmailTemplate.body'
        db.delete_column('emailtemplates_emailtemplate', 'body')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        user_model_label: {
            'Meta': {
                'object_name': User.__name__,
                'db_table': "'%s'" % User._meta.db_table
            },
            User._meta.pk.attname: (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True',
                'db_column': "'%s'" % User._meta.pk.column}
            ),
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'emailtemplates.emailtemplate': {
            'Meta': {'object_name': 'EmailTemplate'},
            'base_template': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'emailtemplate_created'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['%s']" % user_orm_label}),
            'from_address': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'txt_body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'emailtemplate_updated'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['%s']" % user_orm_label})
        }
    }

    complete_apps = ['emailtemplates']
