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
        # Adding model 'ModelTemplate'
        db.create_table('emailtemplates_modeltemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='modeltemplate_created', null=True, on_delete=models.SET_NULL, to=orm[user_orm_label])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='modeltemplate_updated', null=True, on_delete=models.SET_NULL, to=orm[user_orm_label])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('emailtemplates', ['ModelTemplate'])

        # Adding model 'RequiredContextItem'
        db.create_table('emailtemplates_requiredcontextitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='requiredcontextitem_created', null=True, on_delete=models.SET_NULL, to=orm[user_orm_label])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='requiredcontextitem_updated', null=True, on_delete=models.SET_NULL, to=orm[user_orm_label])),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(related_name='required_contexts', to=orm['emailtemplates.ModelTemplate'])),
            ('key', self.gf('django.db.models.fields.SlugField')(max_length=64)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
        ))
        db.send_create_signal('emailtemplates', ['RequiredContextItem'])

        # Adding model 'EmailTemplate'
        db.create_table('emailtemplates_emailtemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='emailtemplate_created', null=True, on_delete=models.SET_NULL, to=orm[user_orm_label])),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='emailtemplate_updated', null=True, on_delete=models.SET_NULL, to=orm[user_orm_label])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('txt_body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('from_address', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
        ))
        db.send_create_signal('emailtemplates', ['EmailTemplate'])


    def backwards(self, orm):
        # Deleting model 'ModelTemplate'
        db.delete_table('emailtemplates_modeltemplate')

        # Deleting model 'RequiredContextItem'
        db.delete_table('emailtemplates_requiredcontextitem')

        # Deleting model 'EmailTemplate'
        db.delete_table('emailtemplates_emailtemplate')


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
        },
        'emailtemplates.modeltemplate': {
            'Meta': {'object_name': 'ModelTemplate'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'modeltemplate_created'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['%s']" % user_orm_label}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'modeltemplate_updated'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['%s']" % user_orm_label})
        },
        'emailtemplates.requiredcontextitem': {
            'Meta': {'object_name': 'RequiredContextItem'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'requiredcontextitem_created'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['%s']" % user_orm_label}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'key': ('django.db.models.fields.SlugField', [], {'max_length': '64'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'required_contexts'", 'to': "orm['emailtemplates.ModelTemplate']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'requiredcontextitem_updated'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['%s']" % user_orm_label})
        }
    }

    complete_apps = ['emailtemplates']
