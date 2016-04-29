Name     : rubygem-railties
Version  : 4.2.3
Release  : 10
URL      : https://rubygems.org/downloads/railties-4.2.3.gem
Source0  : https://rubygems.org/downloads/railties-4.2.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-railties-bin
BuildRequires : ruby
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
= Railties -- Gluing the Engine to the Rails
Railties is responsible for gluing all frameworks together. Overall, it:

%package bin
Summary: bin components for the rubygem-railties package.
Group: Binaries

%description bin
bin components for the rubygem-railties package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n railties-4.2.3
gem spec %{SOURCE0} -l --ruby > rubygem-railties.gemspec

%build
gem build rubygem-railties.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
railties-4.2.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/railties-4.2.3.gem
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/RDOC_MAIN.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/bin/rails
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/all.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/api/task.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/app_rails_loader.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/application.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/application/bootstrap.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/application/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/application/default_middleware_stack.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/application/finisher.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/application/routes_reloader.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/application_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/backtrace_cleaner.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/code_statistics.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/code_statistics_calculator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/commands.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/commands/application.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/commands/commands_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/commands/console.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/commands/dbconsole.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/commands/destroy.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/commands/generate.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/commands/plugin.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/commands/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/commands/server.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/console/app.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/console/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/deprecation.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/engine.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/engine/commands.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/engine/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/engine/railties.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/gem_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/actions.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/actions/create_migration.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/active_model.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/app_base.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/css/assets/assets_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/css/assets/templates/stylesheet.css
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/css/scaffold/scaffold_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/controller/controller_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/controller/templates/view.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/mailer/mailer_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/mailer/templates/layout.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/mailer/templates/layout.text.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/mailer/templates/view.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/mailer/templates/view.text.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/scaffold/scaffold_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/scaffold/templates/_form.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/scaffold/templates/edit.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/scaffold/templates/index.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/scaffold/templates/new.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/erb/scaffold/templates/show.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/generated_attribute.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/js/assets/assets_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/js/assets/templates/javascript.js
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/migration.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/model_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/named_base.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/app_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/app/assets/javascripts/application.js.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/app/assets/stylesheets/application.css
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/app/controllers/application_controller.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/app/helpers/application_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/app/views/layouts/application.html.erb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/bin/bundle
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/bin/rails
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/bin/rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/bin/setup
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config.ru
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/application.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/boot.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/frontbase.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/ibm_db.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/jdbc.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/jdbcmysql.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/jdbcpostgresql.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/jdbcsqlite3.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/mysql.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/oracle.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/postgresql.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/sqlite3.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/databases/sqlserver.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/environment.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/environments/development.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/environments/production.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/environments/test.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/initializers/assets.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/initializers/backtrace_silencers.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/initializers/cookies_serializer.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/initializers/filter_parameter_logging.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/initializers/inflections.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/initializers/mime_types.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/initializers/session_store.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/initializers/wrap_parameters.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/locales/en.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/routes.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/config/secrets.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/db/seeds.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/gitignore
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/public/404.html
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/public/422.html
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/public/500.html
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/public/favicon.ico
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/public/robots.txt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/app/templates/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/assets/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/assets/assets_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/assets/templates/javascript.js
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/assets/templates/stylesheet.css
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/controller/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/controller/controller_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/controller/templates/controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/generator/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/generator/generator_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/generator/templates/%file_name%_generator.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/generator/templates/USAGE.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/generator/templates/templates/.empty_directory
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/helper/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/helper/helper_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/helper/templates/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/integration_test/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/integration_test/integration_test_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/migration/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/migration/migration_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/model/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/model/model_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/plugin/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/plugin/plugin_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/plugin/templates/
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/resource/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/resource/resource_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/resource_route/resource_route_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/scaffold/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/scaffold/scaffold_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/scaffold/templates/scaffold.css
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/scaffold_controller/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/scaffold_controller/scaffold_controller_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/scaffold_controller/templates/controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/task/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/task/task_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/rails/task/templates/task.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/resource_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_case.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/controller/controller_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/controller/templates/functional_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/generator/generator_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/generator/templates/generator_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/helper/helper_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/integration/integration_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/integration/templates/integration_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/job/job_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/job/templates/unit_test.rb.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/mailer/mailer_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/mailer/templates/functional_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/mailer/templates/preview.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/model/model_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/model/templates/fixtures.yml
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/model/templates/unit_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/plugin/plugin_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/plugin/templates/%file_name%_test.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/plugin/templates/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/scaffold/scaffold_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/test_unit/scaffold/templates/functional_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/testing/assertions.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/testing/behaviour.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/generators/testing/setup_and_teardown.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/info.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/info_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/initializable.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/mailers_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/paths.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/rack.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/rack/debugger.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/rack/log_tailer.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/rack/logger.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/railtie.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/railtie/configurable.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/railtie/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/ruby_version_check.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/source_annotation_extractor.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks/annotations.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks/documentation.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks/engine.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks/framework.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks/log.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks/middleware.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks/misc.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks/routes.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks/statistics.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/tasks/tmp.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/templates/layouts/application.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/templates/rails/info/properties.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/templates/rails/info/routes.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/templates/rails/mailers/email.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/templates/rails/mailers/index.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/templates/rails/mailers/mailer.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/templates/rails/welcome/index.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/test_help.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/test_unit/railtie.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/test_unit/sub_test_task.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/test_unit/testing.rake
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/railties-4.2.3/lib/rails/welcome_controller.rb
/usr/lib64/ruby/gems/2.3.0/specifications/railties-4.2.3.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/rails
