from flask import Blueprint, send_from_directory
# from routes import user_routes, home
import os
import importlib

from services.middleware import register_error_handlers


def bootstrap_services(app):

    # REGISTER ALL ROUTES DYNAMICALLY
    with app.app_context():

        basedir = os.path.abspath(os.path.dirname(__file__))
        # Navigate up to the root directory of your project
        routes_dir = os.path.abspath(os.path.join(basedir, '../routes'))

        for filename in os.listdir(routes_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                print(filename)
                # Import the module
                module_name = f'{filename[:-3]}'
                
                print(module_name)
                module_name = f'routes.{module_name}'
                print(module_name)
                module = importlib.import_module(module_name)

                # Register the blueprint
                for attr in dir(module):
                    blueprint = getattr(module, attr)
                    if isinstance(blueprint, Blueprint):
                        if blueprint.name not in app.blueprints:
                            app.register_blueprint(blueprint)
                        else:
                            print(f"Blueprint {blueprint.name} is already registered.")
                        # app.register_blueprint(blueprint)

    # Register error handlers
    register_error_handlers(app)

    # Register middlewares
    # register_middleware(app)


    # Register auth middleware

    # Serve files in the generated directory
    @app.route('/generated/<path:filename>')
    def serve_generated_file(filename):
        return send_from_directory(os.path.join(app.root_path, 'generated'), filename)

