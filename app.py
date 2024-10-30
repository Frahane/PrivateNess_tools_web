from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Detailed breakdown of the PrivateNessTools repository
components = {
    "Key Generation and Management": {
    "Located in": "NessKeys/keys/",
    "Functionality": "Manages various types of keys and configurations for the system, including generation, storage, retrieval, and manipulation of keys.",
    "Usage": "Used to create, load, store, and manipulate different types of keys and configurations essential for secure operations within the PrivateNess ecosystem.",
    "Example": {
        "code": """
from flask import Flask, request, jsonify
from framework.Container import Container
from framework.exceptions import KeyError, ConfigurationError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class KeyManager:
    def __init__(self):
        self.km = Container.KeyManager()

    def generate_key(self, key_type: str, params: dict = None) -> dict:
        try:
            return self.km.generateKey(key_type, params)
        except KeyError as e:
            logger.error(f"Error generating key: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in key generation: {str(e)}")
            raise

    def save_key(self, key_data: dict) -> bool:
        try:
            return self.km.saveKey(key_data)
        except ConfigurationError as e:
            logger.error(f"Error saving key: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in key saving: {str(e)}")
            raise

    def get_key(self, key_id: str) -> dict:
        try:
            return self.km.getKey(key_id)
        except KeyError as e:
            logger.error(f"Error retrieving key: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in key retrieval: {str(e)}")
            raise

    def list_keys(self) -> list:
        try:
            return self.km.showUsersKey()
        except Exception as e:
            logger.error(f"Error listing keys: {str(e)}")
            raise

    def delete_key(self, key_id: str) -> bool:
        try:
            return self.km.deleteKey(key_id)
        except KeyError as e:
            logger.error(f"Error deleting key: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in key deletion: {str(e)}")
            raise

    def export_key(self, key_id: str) -> str:
        try:
            return self.km.exportKey(key_id)
        except KeyError as e:
            logger.error(f"Error exporting key: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in key export: {str(e)}")
            raise

    def import_key(self, key_data: str) -> bool:
        try:
            return self.km.importKey(key_data)
        except ConfigurationError as e:
            logger.error(f"Error importing key: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in key import: {str(e)}")
            raise

@app.route('/keys', methods=['GET'])
def list_keys():
    key_manager = KeyManager()
    try:
        keys = key_manager.list_keys()
        return jsonify({"success": True, "keys": keys})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/keys/generate', methods=['POST'])
def generate_key():
    key_type = request.json.get('type')
    params = request.json.get('params', {})
    key_manager = KeyManager()
    try:
        key = key_manager.generate_key(key_type, params)
        return jsonify({"success": True, "key": key})
    except KeyError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/keys/<key_id>', methods=['GET'])
def get_key(key_id):
    key_manager = KeyManager()
    try:
        key = key_manager.get_key(key_id)
        return jsonify({"success": True, "key": key})
    except KeyError as e:
        return jsonify({"success": False, "error": str(e)}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/keys', methods=['POST'])
def save_key():
    key_data = request.json.get('key_data')
    key_manager = KeyManager()
    try:
        result = key_manager.save_key(key_data)
        return jsonify({"success": True, "result": result})
    except ConfigurationError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/keys/<key_id>', methods=['DELETE'])
def delete_key(key_id):
    key_manager = KeyManager()
    try:
        result = key_manager.delete_key(key_id)
        return jsonify({"success": True, "result": result})
    except KeyError as e:
        return jsonify({"success": False, "error": str(e)}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/keys/export/<key_id>', methods=['GET'])
def export_key(key_id):
    key_manager = KeyManager()
    try:
        exported_key = key_manager.export_key(key_id)
        return jsonify({"success": True, "exported_key": exported_key})
    except KeyError as e:
        return jsonify({"success": False, "error": str(e)}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/keys/import', methods=['POST'])
def import_key():
    key_data = request.json.get('key_data')
    key_manager = KeyManager()
    try:
        result = key_manager.import_key(key_data)
        return jsonify({"success": True, "result": result})
    except ConfigurationError as e:
        return jsonify({"success": False, "error": str(e)}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
        """,
        "Key Generation and Management API Implementation:": """
GET /keys - List all keys
POST /keys/generate - Generate a new key (requires 'type' and optional 'params' in request body)
GET /keys/<key_id> - Get a specific key
POST /keys - Save a key (requires 'key_data' in request body)
DELETE /keys/<key_id> - Delete a specific key
GET /keys/export/<key_id> - Export a specific key
POST /keys/import - Import a key (requires 'key_data' in request body)

Response Formats:
- Success Response: {"success": true, "data": <result>}
- Error Response: {"success": false, "error": <error_message>}

Status Codes:
- 200: Successful operation
- 400: Invalid input or configuration error
- 404: Key not found
- 500: Internal server error
        """
    }
},
    "Node Management": {
    "Functionality": "Updates the list of service nodes from the blockchain.",
    "Usage": "Ensures the application is using the latest nodes for file operations.",
    "Example": {
        "code": '''
from flask import Flask, request, jsonify
from framework.Container import Container
from framework.NodeManager import NodeStatus, NodeInfo
from framework.exceptions import NodeConnectionError, NodeValidationError
import validators
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class NodeManager:
    def __init__(self):
        self.nm = Container.NodeManager()

    def list_nodes(self) -> List[Dict]:
        """List all available nodes with their status"""
        try:
            nodes = self.nm.listNodes()
            return [{"url": node.url, "status": node.status.value} for node in nodes]
        except Exception as e:
            logger.error(f"Error listing nodes: {str(e)}")
            raise

    def select_node(self, node_url: str) -> bool:
        """Select a specific node for operations"""
        if not validators.url(node_url):
            raise NodeValidationError("Invalid node URL format")
        try:
            return self.nm.select(node_url)
        except Exception as e:
            logger.error(f"Error selecting node {node_url}: {str(e)}")
            raise

    def update_nodes_from_blockchain(self) -> bool:
        """Update nodes list from blockchain"""
        try:
            return self.nm.updateNodesFromBlockchain()
        except Exception as e:
            logger.error(f"Error updating nodes from blockchain: {str(e)}")
            raise

    def get_node_info(self, node_url: str) -> NodeInfo:
        """Get detailed information about a specific node"""
        if not validators.url(node_url):
            raise NodeValidationError("Invalid node URL format")
        try:
            return self.nm.info(node_url)
        except Exception as e:
            logger.error(f"Error getting info for node {node_url}: {str(e)}")
            raise

    def check_node_status(self, node_url: str) -> NodeStatus:
        """Check the current status of a specific node"""
        if not validators.url(node_url):
            raise NodeValidationError("Invalid node URL format")
        try:
            return self.nm.checkStatus(node_url)
        except Exception as e:
            logger.error(f"Error checking status for node {node_url}: {str(e)}")
            raise

    def get_active_node(self) -> Optional[str]:
        """Get currently active node"""
        try:
            return self.nm.getActiveNode()
        except Exception as e:
            logger.error(f"Error getting active node: {str(e)}")
            raise

@app.route("/nodes", methods=["GET"])
def list_nodes():
    """API endpoint to list all nodes"""
    node_manager = NodeManager()
    try:
        nodes = node_manager.list_nodes()
        return jsonify({
            "success": True,
            "nodes": nodes
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/nodes/select", methods=["POST"])
def select_node():
    """API endpoint to select a node"""
    node_url = request.json.get("node_url")
    if not node_url:
        return jsonify({
            "success": False,
            "error": "node_url is required"
        }), 400

    node_manager = NodeManager()
    try:
        result = node_manager.select_node(node_url)
        return jsonify({
            "success": True,
            "result": result
        })
    except NodeValidationError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except NodeConnectionError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 503
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/nodes/update", methods=["POST"])
def update_nodes():
    """API endpoint to update nodes from blockchain"""
    node_manager = NodeManager()
    try:
        result = node_manager.update_nodes_from_blockchain()
        return jsonify({
            "success": True,
            "result": result
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/nodes/<path:node_url>/info", methods=["GET"])
def get_node_info(node_url):
    """API endpoint to get node information"""
    node_manager = NodeManager()
    try:
        info = node_manager.get_node_info(node_url)
        return jsonify({
            "success": True,
            "info": info.__dict__
        })
    except NodeValidationError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/nodes/<path:node_url>/status", methods=["GET"])
def check_node_status(node_url):
    """API endpoint to check node status"""
    node_manager = NodeManager()
    try:
        status = node_manager.check_node_status(node_url)
        return jsonify({
            "success": True,
            "status": status.value
        })
    except NodeValidationError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/nodes/active", methods=["GET"])
def get_active_node():
    """API endpoint to get currently active node"""
    node_manager = NodeManager()
    try:
        active_node = node_manager.get_active_node()
        return jsonify({
            "success": True,
            "active_node": active_node
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
''',
        "Node Management API Implementation Documentation:": '''
GET /nodes - List all available nodes and their status
POST /nodes/select - Select a specific node (requires 'node_url' in request body)
POST /nodes/update - Update nodes list from blockchain
GET /nodes/<node_url>/info - Get detailed information about a specific node
GET /nodes/<node_url>/status - Check the status of a specific node
GET /nodes/active - Get the currently active node

Response Formats:
- Success Response: {"success": true, "data": <result>}
- Error Response: {"success": false, "error": <error_message>}

Status Codes:
- 200: Successful operation
- 400: Invalid input/validation error
- 503: Node connection error
- 500: Internal server error
'''
    }
},
    "User Management": {
    "Functionality": [
        "User Listing: Retrieve a list of users.",
        "User Selection: Select a specific user for operations.",
        "User Registration Check: Check if the current user is registered on the blockchain.",
        "User NVS (Name-Value Store): Retrieve the NVS associated with the user.",
        "User Key Management: Generate and manage user keys.",
    ],
    "Usage": "Ensures users are registered and manages their associated data and keys.",
    "Example": {
        "code": '''
from flask import Flask, request, jsonify
from framework.Container import Container
from framework.exceptions import UserNotFoundError, UserRegistrationError
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class UserManager:
    def __init__(self):
        self.um = Container.UserManager()
        self.km = Container.KeyManager()

    def list_users(self) -> List[str]:
        """Retrieve a list of all users"""
        try:
            return self.um.showUsersKey()
        except Exception as e:
            logger.error(f"Error listing users: {str(e)}")
            raise

    def select_user(self, username: str) -> bool:
        """Select a specific user for operations"""
        try:
            self.um.changeCurrentUser(username)
            return True
        except Exception as e:
            logger.error(f"Error selecting user {username}: {str(e)}")
            raise

    def check_user_registration(self, username: str) -> bool:
        """Check if a user is registered on the blockchain"""
        try:
            return self.um.checkUser(username)
        except Exception as e:
            logger.error(f"Error checking registration for user {username}: {str(e)}")
            raise

    def get_user_nvs(self, username: str) -> Dict:
        """Retrieve the NVS associated with a user"""
        try:
            return self.um.getUserNVS(username)
        except Exception as e:
            logger.error(f"Error retrieving NVS for user {username}: {str(e)}")
            raise

    def generate_user_key(self, username: str, key_type: str) -> Dict:
        """Generate a new key for a user"""
        try:
            return self.km.generateUserKey(username, key_type)
        except Exception as e:
            logger.error(f"Error generating key for user {username}: {str(e)}")
            raise

    def get_current_user(self) -> Optional[str]:
        """Get the currently selected user"""
        try:
            return self.um.getCurrentUser()
        except Exception as e:
            logger.error(f"Error getting current user: {str(e)}")
            raise

@app.route("/users", methods=["GET"])
def list_users():
    """API endpoint to list all users"""
    user_manager = UserManager()
    try:
        users = user_manager.list_users()
        return jsonify({
            "success": True,
            "users": users
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/users/select/<username>", methods=["POST"])
def select_user(username):
    """API endpoint to select a user"""
    user_manager = UserManager()
    try:
        result = user_manager.select_user(username)
        return jsonify({
            "success": True,
            "message": f"User {username} selected successfully"
        })
    except UserNotFoundError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/users/check/<username>", methods=["GET"])
def check_user_registration(username):
    """API endpoint to check user registration"""
    user_manager = UserManager()
    try:
        is_registered = user_manager.check_user_registration(username)
        return jsonify({
            "success": True,
            "registered": is_registered
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/users/<username>/nvs", methods=["GET"])
def get_user_nvs(username):
    """API endpoint to get user NVS"""
    user_manager = UserManager()
    try:
        nvs = user_manager.get_user_nvs(username)
        return jsonify({
            "success": True,
            "nvs": nvs
        })
    except UserNotFoundError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/users/<username>/generate_key", methods=["POST"])
def generate_user_key(username):
    """API endpoint to generate a new key for a user"""
    key_type = request.json.get("key_type")
    if not key_type:
        return jsonify({
            "success": False,
            "error": "key_type is required"
        }), 400

    user_manager = UserManager()
    try:
        key = user_manager.generate_user_key(username, key_type)
        return jsonify({
            "success": True,
            "key": key
        })
    except UserNotFoundError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/users/current", methods=["GET"])
def get_current_user():
    """API endpoint to get the currently selected user"""
    user_manager = UserManager()
    try:
        current_user = user_manager.get_current_user()
        return jsonify({
            "success": True,
            "current_user": current_user
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
''',
        "User Management API Implementation Documentation:": '''
GET /users - List all users
POST /users/select/<username> - Select a specific user
GET /users/check/<username> - Check if a user is registered
GET /users/<username>/nvs - Get the NVS associated with a user
POST /users/<username>/generate_key - Generate a new key for a user (requires 'key_type' in request body)
GET /users/current - Get the currently selected user

Response Formats:
- Success Response: {"success": true, "data": <result>}
- Error Response: {"success": false, "error": <error_message>}

Status Codes:
- 200: Successful operation
- 400: Invalid input
- 404: User not found
- 500: Internal server error
'''
    }
},
    "File Management": {
    "Functionality": [
        "File Upload: Upload files to the system, with optional encryption.",
        "File Download: Download files from the system, with automatic decryption if needed.",
        "File Listing: List files in the current directory or a specified path.",
        "File Information: Retrieve detailed information about a specific file.",
        "Directory Operations: Create, remove, and navigate directories.",
        "File Tree: Display the file structure in a tree format."
    ],
    "Usage": "Allows users to securely manage their files and directories within the PrivateNess system.",
    "Example": {
        "code": '''
from flask import Flask, request, jsonify, send_file
from framework.Container import Container
from framework.exceptions import FileNotFoundError, EncryptionError, DirectoryError
from werkzeug.utils import secure_filename
from typing import List, Dict
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class FileManager:
    def __init__(self):
        self.fm = Container.FileManager()

    def upload_file(self, file, encrypt: bool = False) -> Dict:
        """Upload a file, with optional encryption"""
        try:
            filename = secure_filename(file.filename)
            if encrypt:
                return self.fm.UploadEncrypt(file)
            else:
                return self.fm.upload(file)
        except EncryptionError as e:
            logger.error(f"Encryption error during file upload: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error uploading file: {str(e)}")
            raise

    def download_file(self, shadowname: str) -> str:
        """Download a file by its shadowname"""
        try:
            return self.fm.download(shadowname)
        except FileNotFoundError as e:
            logger.error(f"File not found: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error downloading file: {str(e)}")
            raise

    def list_files(self, path: str = ".") -> List[Dict]:
        """List files in the specified directory"""
        try:
            return self.fm.ls(path)
        except Exception as e:
            logger.error(f"Error listing files: {str(e)}")
            raise

    def file_info(self, shadowname: str) -> Dict:
        """Get detailed information about a file"""
        try:
            return self.fm.fileinfo(shadowname)
        except FileNotFoundError as e:
            logger.error(f"File not found: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error getting file info: {str(e)}")
            raise

    def create_directory(self, path: str) -> bool:
        """Create a new directory"""
        try:
            return self.fm.mkdir(path)
        except DirectoryError as e:
            logger.error(f"Error creating directory: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error creating directory: {str(e)}")
            raise

    def remove_directory(self, path: str) -> bool:
        """Remove a directory"""
        try:
            return self.fm.rmdir(path)
        except DirectoryError as e:
            logger.error(f"Error removing directory: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error removing directory: {str(e)}")
            raise

    def change_directory(self, path: str) -> bool:
        """Change the current working directory"""
        try:
            return self.fm.cd(path)
        except DirectoryError as e:
            logger.error(f"Error changing directory: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error changing directory: {str(e)}")
            raise

    def get_file_tree(self, path: str = ".") -> str:
        """Get the file structure in a tree format"""
        try:
            return self.fm.tree(path)
        except Exception as e:
            logger.error(f"Error getting file tree: {str(e)}")
            raise

@app.route("/files/upload", methods=["POST"])
def upload_file():
    """API endpoint to upload a file"""
    if "file" not in request.files:
        return jsonify({
            "success": False,
            "error": "No file part in the request"
        }), 400
    file = request.files["file"]
    encrypt = request.form.get("encrypt", "false").lower() == "true"
    file_manager = FileManager()
    try:
        result = file_manager.upload_file(file, encrypt)
        return jsonify({
            "success": True,
            "file": result
        })
    except EncryptionError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/files/download/<shadowname>", methods=["GET"])
def download_file(shadowname):
    """API endpoint to download a file"""
    file_manager = FileManager()
    try:
        file_path = file_manager.download_file(shadowname)
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/files/list", methods=["GET"])
def list_files():
    """API endpoint to list files"""
    path = request.args.get("path", ".")
    file_manager = FileManager()
    try:
        files = file_manager.list_files(path)
        return jsonify({
            "success": True,
            "files": files
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/files/info/<shadowname>", methods=["GET"])
def file_info(shadowname):
    """API endpoint to get file information"""
    file_manager = FileManager()
    try:
        info = file_manager.file_info(shadowname)
        return jsonify({
            "success": True,
            "info": info
        })
    except FileNotFoundError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/directories", methods=["POST"])
def create_directory():
    """API endpoint to create a directory"""
    path = request.json.get("path")
    if not path:
        return jsonify({
            "success": False,
            "error": "Path is required"
        }), 400
    file_manager = FileManager()
    try:
        result = file_manager.create_directory(path)
        return jsonify({
            "success": True,
            "result": result
        })
    except DirectoryError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/directories", methods=["DELETE"])
def remove_directory():
    """API endpoint to remove a directory"""
    path = request.json.get("path")
    if not path:
        return jsonify({
            "success": False,
             "error": "Path is required"
        }), 400
    file_manager = FileManager()
    try:
        result = file_manager.remove_directory(path)
        return jsonify({
            "success": True,
            "result": result
        })
    except DirectoryError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/directories", methods=["PUT"])
def change_directory():
    """API endpoint to change the current directory"""
    path = request.json.get("path")
    if not path:
        return jsonify({
            "success": False,
            "error": "Path is required"
        }), 400
    file_manager = FileManager()
    try:
        result = file_manager.change_directory(path)
        return jsonify({
            "success": True,
            "result": result
        })
    except DirectoryError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/directories/tree", methods=["GET"])
def get_file_tree():
    """API endpoint to get the file structure in a tree format"""
    path = request.args.get("path", ".")
    file_manager = FileManager()
    try:
        tree = file_manager.get_file_tree(path)
        return jsonify({
            "success": True,
            "tree": tree
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
''',
        "File Management API Implementation Documentation:": '''
POST /files/upload - Upload a file, with optional encryption
GET /files/download/<shadowname> - Download a file by its shadowname
GET /files/list - List files in the specified directory
GET /files/info/<shadowname> - Get detailed information about a file
POST /directories - Create a new directory
DELETE /directories - Remove a directory
PUT /directories - Change the current working directory
GET /directories/tree - Get the file structure in a tree format

Response Formats:
- Success Response: {"success": true, "data": <result>}
- Error Response: {"success": false, "error": <error_message>}

Status Codes:
- 200: Successful operation
- 400: Invalid input
- 404: File not found
- 500: Internal server error
'''
    }
},
    "Backup and Restore": {
    "Functionality": [
        "Backup Creation: Create a backup of keys and configurations.",
        "Backup Restoration: Restore keys and configurations from a backup file or address.",
        "Backup Verification: Verify the integrity of a backup before restoration."
    ],
    "Usage": "Ensures data integrity and availability by allowing users to create and restore backups of their configurations and keys.",
    "Example": {
        "code": '''
from flask import Flask, request, jsonify
from framework.Container import Container
from framework.exceptions import BackupError, RestoreError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class BackupManager:
    def __init__(self):
        self.bm = Container.Backup()

    def create_backup(self) -> str:
        """Create a backup of keys and configurations"""
        try:
            return self.bm.backup()
        except Exception as e:
            logger.error(f"Error creating backup: {str(e)}")
            raise

    def restore_backup(self, filename: str) -> bool:
        """Restore keys and configurations from a backup file"""
        try:
            return self.bm.restore(filename)
        except RestoreError as e:
            logger.error(f"Error restoring backup: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error restoring backup: {str(e)}")
            raise

    def verify_backup(self, filename: str) -> bool:
        """Verify the integrity of a backup file"""
        try:
            return self.bm.verify(filename)
        except Exception as e:
            logger.error(f"Error verifying backup: {str(e)}")
            raise

@app.route("/backup", methods=["POST"])
def create_backup():
    """API endpoint to create a backup"""
    backup_manager = BackupManager()
    try:
        result = backup_manager.create_backup()
        return jsonify({
            "success": True,
            "result": result
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/backup/restore", methods=["POST"])
def restore_backup():
    """API endpoint to restore a backup"""
    filename = request.json.get("filename")
    if not filename:
        return jsonify({
            "success": False,
            "error": "filename is required"
        }), 400

    backup_manager = BackupManager()
    try:
        result = backup_manager.restore_backup(filename)
        return jsonify({
            "success": True,
            "result": result
        })
    except RestoreError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/backup/verify", methods=["POST"])
def verify_backup():
    """API endpoint to verify a backup"""
    filename = request.json.get("filename")
    if not filename:
        return jsonify({
            "success": False,
            "error": "filename is required"
        }), 400

    backup_manager = BackupManager()
    try:
        is_valid = backup_manager.verify_backup(filename)
        return jsonify({
            "success": True,
            "valid": is_valid
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
''',
        "Backup and Restore API Implementation Documentation:": '''
POST /backup - Create a backup of keys and configurations
POST /backup/restore - Restore keys and configurations from a backup file (requires 'filename' in request body)
POST /backup/verify - Verify the integrity of a backup file (requires 'filename' in request body)

Response Formats:
- Success Response: {"success": true, "data": <result>}
- Error Response: {"success": false, "error": <error_message>}

Status Codes:
- 200: Successful operation
- 400: Invalid input
- 500: Internal server error
'''
    }
},
    "Random Number Generation (PRNG)": {
    "Functionality": [
        "Generate Random Number: Produce a cryptographically secure random number.",
        "Generate Random String: Create a random string of specified length.",
        "Generate Random Bytes: Produce random bytes of specified length.",
        "Seed PRNG: Manually seed the PRNG for deterministic output (use with caution)."
    ],
    "Usage": "Provides cryptographically secure random numbers and strings for various security-critical operations within the system.",
    "Example": {
        "code": '''
from flask import Flask, request, jsonify
from framework.Container import Container
from framework.exceptions import PRNGError
import base64
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class RandomManager:
    def __init__(self):
        self.prng = Container.Prng()

    def generate_random_number(self, min_value: int = 0, max_value: int = 2**32) -> int:
        """Generate a random number within the specified range"""
        try:
            return self.prng.generate_int(min_value, max_value)
        except PRNGError as e:
            logger.error(f"Error generating random number: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in random number generation: {str(e)}")
            raise

    def generate_random_string(self, length: int) -> str:
        """Generate a random string of specified length"""
        try:
            return self.prng.generate_string(length)
        except PRNGError as e:
            logger.error(f"Error generating random string: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in random string generation: {str(e)}")
            raise

    def generate_random_bytes(self, length: int) -> bytes:
        """Generate random bytes of specified length"""
        try:
            return self.prng.generate_bytes(length)
        except PRNGError as e:
            logger.error(f"Error generating random bytes: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in random bytes generation: {str(e)}")
            raise

    def seed_prng(self, seed: str) -> bool:
        """Manually seed the PRNG (use with caution)"""
        try:
            return self.prng.seed(seed)
        except PRNGError as e:
            logger.error(f"Error seeding PRNG: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in PRNG seeding: {str(e)}")
            raise

@app.route("/random/number", methods=["GET"])
def get_random_number():
    """API endpoint to get a random number"""
    min_value = request.args.get("min", 0, type=int)
    max_value = request.args.get("max", 2**32, type=int)
    random_manager = RandomManager()
    try:
        number = random_manager.generate_random_number(min_value, max_value)
        return jsonify({
            "success": True,
            "number": number
        })
    except PRNGError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/random/string", methods=["GET"])
def get_random_string():
    """API endpoint to get a random string"""
    length = request.args.get("length", 32, type=int)
    random_manager = RandomManager()
    try:
        string = random_manager.generate_random_string(length)
        return jsonify({
            "success": True,
            "string": string
        })
    except PRNGError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/random/bytes", methods=["GET"])
def get_random_bytes():
    """API endpoint to get random bytes"""
    length = request.args.get("length", 32, type=int)
    random_manager = RandomManager()
    try:
        bytes_data = random_manager.generate_random_bytes(length)
        return jsonify({
            "success": True,
            "bytes": base64.b64encode(bytes_data).decode('utf-8')
        })
    except PRNGError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/random/seed", methods=["POST"])
def seed_prng():
    """API endpoint to seed the PRNG (use with caution)"""
    seed = request.json.get("seed")
    if not seed:
        return jsonify({
            "success": False,
            "error": "seed is required"
        }), 400

    random_manager = RandomManager()
    try:
        result = random_manager.seed_prng(seed)
        return jsonify({
            "success": True,
            "result": result
        })
    except PRNGError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
''',
        "Random Number Generation (PRNG) API Implementation Documentation:": '''
GET /random/number - Generate a random number (optional query parameters: min, max)
GET /random/string - Generate a random string (optional query parameter: length)
GET /random/bytes - Generate random bytes (optional query parameter: length)
POST /random/seed - Seed the PRNG (requires 'seed' in request body)

Response Formats:
- Success Response: {"success": true, "data": <result>}
- Error Response: {"success": false, "error": <error_message>}

Status Codes:
- 200: Successful operation
- 400: Invalid input
- 500: Internal server error

Note: The /random/seed endpoint should be used with caution as it affects the randomness of the PRNG.
'''
    }
},
    "Blockchain Interaction": {
    "Functionality": [
        "Blockchain Node Connection: Establish and manage connections to blockchain nodes.",
        "Transaction Management: Create, sign, and broadcast transactions.",
        "NVS Operations: Interact with the Name-Value Storage system.",
        "Block Information: Retrieve and validate block information.",
        "Network Status: Monitor blockchain network status and synchronization.",
        "Smart Contract Integration: Interact with blockchain smart contracts."
    ],
    "Usage": "Enables secure and decentralized operations through blockchain integration.",
    "Example": {
        "code": '''
from flask import Flask, request, jsonify
from framework.Container import Container
from framework.exceptions import (
    BlockchainConnectionError,
    TransactionError,
    NVSError,
    SmartContractError
)
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

class BlockchainManager:
    def __init__(self):
        self.blockchain = Container.Blockchain()
        self.rpc = Container.BlockchainRPC()

    def connect_node(self, node_url: str, credentials: Dict) -> bool:
        """Establish connection to a blockchain node"""
        try:
            return self.rpc.connect(node_url, credentials)
        except BlockchainConnectionError as e:
            logger.error(f"Error connecting to blockchain node: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in node connection: {str(e)}")
            raise

    def get_blockchain_info(self) -> Dict:
        """Retrieve current blockchain information"""
        try:
            return self.rpc.get_info()
        except BlockchainConnectionError as e:
            logger.error(f"Error getting blockchain info: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error getting blockchain info: {str(e)}")
            raise

    def create_transaction(self, tx_data: Dict) -> str:
        """Create and sign a new transaction"""
        try:
            return self.blockchain.create_transaction(tx_data)
        except TransactionError as e:
            logger.error(f"Error creating transaction: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in transaction creation: {str(e)}")
            raise

    def broadcast_transaction(self, tx_hex: str) -> str:
        """Broadcast a signed transaction to the network"""
        try:
            return self.blockchain.send_raw_transaction(tx_hex)
        except TransactionError as e:
            logger.error(f"Error broadcasting transaction: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in transaction broadcast: {str(e)}")
            raise

    def get_nvs_value(self, name: str) -> Dict:
        """Retrieve value from Name-Value Storage"""
        try:
            return self.blockchain.get_nvs(name)
        except NVSError as e:
            logger.error(f"Error retrieving NVS value: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in NVS retrieval: {str(e)}")
            raise

    def set_nvs_value(self, name: str, value: str, days: int = 365) -> str:
        """Set value in Name-Value Storage"""
        try:
            return self.blockchain.set_nvs(name, value, days)
        except NVSError as e:
            logger.error(f"Error setting NVS value: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in NVS setting: {str(e)}")
            raise

    def get_block_info(self, block_hash: str) -> Dict:
        """Retrieve information about a specific block"""
        try:
            return self.rpc.get_block(block_hash)
        except BlockchainConnectionError as e:
            logger.error(f"Error getting block info: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error getting block info: {str(e)}")
            raise

    def execute_smart_contract(self, contract_address: str, method: str, params: Dict) -> Dict:
        """Execute a smart contract method"""
        try:
            return self.blockchain.execute_contract(contract_address, method, params)
        except SmartContractError as e:
            logger.error(f"Error executing smart contract: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in smart contract execution: {str(e)}")
            raise

@app.route("/blockchain/connect", methods=["POST"])
def connect_node():
    """API endpoint to connect to a blockchain node"""
    node_url = request.json.get("node_url")
    credentials = request.json.get("credentials", {})
    
    if not node_url:
        return jsonify({
            "success": False,
            "error": "node_url is required"
        }), 400

    blockchain_manager = BlockchainManager()
    try:
        result = blockchain_manager.connect_node(node_url, credentials)
        return jsonify({
            "success": True,
            "connected": result
        })
    except BlockchainConnectionError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/blockchain/info", methods=["GET"])
def get_blockchain_info():
    """API endpoint to get blockchain information"""
    blockchain_manager = BlockchainManager()
    try:
        info = blockchain_manager.get_blockchain_info()
        return jsonify({
            "success": True,
            "info": info
        })
    except BlockchainConnectionError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/blockchain/transaction", methods=["POST"])
def create_and_broadcast_transaction():
    """API endpoint to create and broadcast a transaction"""
    tx_data = request.json.get("tx_data")
    if not tx_data:
        return jsonify({
            "success": False,
            "error": "tx_data is required"
        }), 400

    blockchain_manager = BlockchainManager()
    try:
        # Create and sign transaction
        tx_hex = blockchain_manager.create_transaction(tx_data)
        # Broadcast transaction
        tx_id = blockchain_manager.broadcast_transaction(tx_hex)
        return jsonify({
            "success": True,
            "transaction_id": tx_id
        })
    except TransactionError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/blockchain/nvs/<name>", methods=["GET"])
def get_nvs_value(name):
    """API endpoint to get NVS value"""
    blockchain_manager = BlockchainManager()
    try:
        value = blockchain_manager.get_nvs_value(name)
        return jsonify({
            "success": True,
            "value": value
        })
    except NVSError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/blockchain/nvs/<name>", methods=["POST"])
def set_nvs_value(name):
    """API endpoint to set NVS value"""
    value = request.json.get("value")
    days = request.json.get("days", 365)
    if not value:
        return jsonify({
            "success": False,
            "error": "value is required"
        }), 400

    blockchain_manager = BlockchainManager()
    try:
        result = blockchain_manager.set_nvs_value(name, value, days)
        return jsonify({
            "success": True,
            "result": result
        })
    except NVSError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/blockchain/block/<block_hash>", methods=["GET"])
def get_block_info(block_hash):
    """API endpoint to get block information"""
    blockchain_manager = BlockchainManager()
    try:
        info = blockchain_manager.get_block_info(block_hash)
        return jsonify({
            "success": True,
            "info": info
        })
    except BlockchainConnectionError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route("/blockchain/smart_contract/<contract_address>/<method>", methods=["POST"])
def execute_smart_contract(contract_address, method):
    """API endpoint to execute a smart contract method"""
    params = request.json.get("params", {})
    blockchain_manager = BlockchainManager()
    try:
        result = blockchain_manager.execute_smart_contract(contract_address, method, params)
        return jsonify({
            "success": True,
            "result": result
        })
    except SmartContractError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
''',
        "Blockchain Interaction API Implementation Documentation:": '''
POST /blockchain/connect - Connect to a blockchain node (required: node_url, optional: credentials)
GET /blockchain/info - Get blockchain information
POST /blockchain/transaction - Create and broadcast a transaction (required: tx_data)
GET /blockchain/nvs/<name> - Get NVS value
POST /blockchain/nvs/<name> - Set NVS value (required: value, optional: days)
GET /blockchain/block/<block_hash> - Get block information
POST /blockchain/smart_contract/<contract_address>/<method> - Execute a smart contract method (optional: params)

Response Formats:
- Success Response: {"success": true, "data": <result>}
- Error Response: {"success": false, "error": <error_message>}

Status Codes:
- 200: Successful operation
- 400: Invalid input
- 500: Internal server error

Note: The /blockchain/connect endpoint should be used with caution as it affects the blockchain connection.
'''
    }
}
}

repository_info = {
    "description": "The PrivatenessTools repository provides a set of console tools designed for interacting with the Privateness service node, which focuses on secure file storage and user management through the Emercoin blockchain.",
    "target_audience": "Software engineers, developers, and frontend developers looking to build applications using these tools."
}

dependencies = [
    "humanize: For human-friendly formatting of data.",
    "requests: For making HTTP requests to the service nodes.",
    "pynacl: For cryptographic operations, particularly for signing and verifying messages.",
    "pycryptodome: For encryption and decryption of files.",
    "prettytable: For displaying tabular data in a readable format.",
    "validators: For validating URLs and other data formats.",
    "lxml: For XML processing.",
    "libxslt: For XSLT transformations.",
    "random-word: For generating random words, potentially for user or file naming."
]

@app.route('/')
def index():
    component_icons = {
        "Key Generation and Management": "key",
        "Node Management": "device_hub",
        "User Management": "people",
        "File Management": "folder",
        "Backup and Restore": "backup",
        "Random Number Generation (PRNG)": "casino",
        "Blockchain Interaction": "link"
    }
    
    return render_template('index.html', 
                         repository_info=repository_info, 
                         components=components, 
                         dependencies=dependencies,
                         component_icons=component_icons)

if __name__ == '__main__':
    app.run(debug=True)