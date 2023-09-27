from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = { name }, views = { views }, likes = { likes })"

# Run one time to avoid override data
# db.create_all()

video_post_args = reqparse.RequestParser()
video_post_args.add_argument("name", type=str, help="Name of video is required", required=True)
video_post_args.add_argument("views", type=str, help="Views of video")
video_post_args.add_argument("likes", type=str, help="Likes on video")



video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument("name", type=str, help="Name of the video is required")
video_patch_args.add_argument("views", type=int, help="Views of the video")
video_patch_args.add_argument("likes", type=int, help="Likes on the video")


# videos = {}

# def abort_if_video_doesnt_exist(video_id):
#     if video_id not in videos:
#         abort(404, message="Video ID is not valid!")

# def abort_if_video_exist(video_id):
#     if video_id in videos:
#         abort(409, message=f"Video already exists with ID {video_id}!")

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that ID!")
        return result
        # abort_if_video_doesnt_exist(video_id)
        # return videos[video_id]

    @marshal_with(resource_fields)
    def post(self, video_id):
        # abort_if_video_exist(video_id)
        # args = video_post_args.parse_args()
        # videos[video_id] = args
        # return videos[video_id], 201
        args = video_post_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video ID does exist")

        video = VideoModel(id= video_id, name= args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_patch_args.parse_args()
        video = VideoModel.query.filter_by(id=video_id).first()

        if not video:
            abort(404, message="Video doesn't exists, cannot update!")

        # for key in args:
        #     if hasattr(video, key):
        #        setattr(video, key, args[key])
        
        attributes_to_update = ["name", "views", "likes"]
        
        for attribute in attributes_to_update:
            if args.get(attribute):
                setattr(video, attribute, args[attribute])

        db.session.commit()
        return video

    def delete(self, video_id):
        # abort_if_video_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204

api.add_resource(Video, "/video/<int:video_id>")


# class HelloWorld(Resource):
#     def get(self, name, test):
#         return { "name": name, "test": test  }

#     def post(self):
#         return { "data": "Posted" }


# api.add_resource(HelloWorld, "/helloWorld/<string:name>/<int:test>")

if __name__ == "__main__":
    # only for development "debug = True"
    app.run(debug=True)
