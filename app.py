from flask import Flask, request, jsonify
from flask_cors import CORS
from config import db, SECRET_KEY
from os import path, getcwd, environ
from dotenv import load_dotenv
from models.user import User
from models.projects import Projects
from models.experiences import Experiences
from models.educations import Educations
from models.skills import Skills
from models.certificates import Certificates
from models.peronalDetails import PersonalDetails

load_dotenv(path.join(getcwd(),'.env'))

def create_app():
    app =Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.secret_key = SECRET_KEY

    db.init_app(app)
    print("DB Initialized successfully")
    
    with app.app_context():
        @app.route("/signup", methods=['POST'])
        def signup():
            data = request.form.to_dict(flat=True)

            new_user = User(
                username = data['username']
            )

            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg="User added successfully")

        @app.route("/add_personal_details", methods=['POST'])
        def add_personal_details():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username=recv_username).first()

            personal_data = request.get_json()

            new_personal_details = PersonalDetails(
                name=personal_data['name'],
                email=personal_data['email'],
                phone=personal_data['phone'],
                address=personal_data['address'],
                linkedin_url=personal_data['linkedin_url'],
                user_id=user.id
            )
            db.session.add(new_personal_details)
            db.session.commit()
            return jsonify(msg="Personal details added successfully")

        @app.route('/add_project', methods=['POST'])
        def add_project():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username=recv_username).first()

            project_data = request.get_json()
            
            for project in project_data["data"]:
                new_project = Projects(
                    name=project['name'],
                    desc=project['desc'],
                    start_date=project['start_date'],
                    end_date=project['end_date'],
                    user_id=user.id
                )
                db.session.add(new_project)
                db.session.commit()
                return jsonify(msg="Project details added successfully")

        @app.route('/add_skills', methods=['POST'])
        def add_skills():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username=recv_username).first()

            skills_data = request.get_json()
            
            for skill in skills_data["data"]:
                new_skill = Skills(
                    title=skill['title'],
                    confidence_score=skill['confidence_score'],
                    user_id=user.id
                )
                db.session.add(new_skill)
                db.session.commit()
                return jsonify(msg="Skills details added successfully")

        @app.route('/add_experience', methods=['POST'])
        def add_experience():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username=recv_username).first()

            experience_data = request.get_json()
            
            for experience in experience_data["data"]:
                new_experience = Experiences(
                    company_name=experience['company_name'],
                    role=experience['role'],
                    role_desc=experience['role_desc'],
                    start_date=experience['start_date'],
                    end_date=experience['end_date'],
                    user_id=user.id
                )
                db.session.add(new_experience)
                db.session.commit()
                return jsonify(msg="Experiences details added successfully")

        @app.route('/add_education', methods=['POST'])
        def add_education():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username=recv_username).first()

            education_data = request.get_json()
            
            for education in education_data["data"]:
                new_education = Educations(
                    school_name=education['school_name'],
                    degree_name=education['degree_name'],
                    start_date=education['start_date'],
                    end_date=education['end_date'],
                    user_id=user.id
                )
                db.session.add(new_education)
                db.session.commit()
                return jsonify(msg="Educations details added successfully")

        @app.route('/add_certificate', methods=['POST'])
        def add_certificate():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username=recv_username).first()

            certificate_data = request.get_json()
            
            for certificate in certificate_data["data"]:
                new_certificate = Certificates(
                    title=certificate['school_name'],
                    start_date=certificate['start_date'],
                    end_date=certificate['end_date'],
                    user_id=user.id
                )
                db.session.add(new_certificate)
                db.session.commit()
                return jsonify(msg="Certificates details added successfully")

        @app.route("/get_resume_json", methods=["GET"])
        def get_resume_json():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username=recv_username).first()

            personal_details = PersonalDetails.query.filter_by(user_id=user.id).first()
            experiences = Experiences.query.filter_by(user_id=user.id)
            projects = Projects.query.filter_by(user_id=user.id)
            educations = Educations.query.filter_by(user_id=user.id)
            certificates = Certificates.query.filter_by(user_id=user.id)
            skills = Skills.query.filter_by(user_id=user.id)

            resume_data ={
                "name":personal_details.name,
                "email":personal_details.email,
                "phone":personal_details.phone,
                "address":personal_details.address,
                "linkedin_url":personal_details.linkedin_url
            }

           

            experiences_data = []
            projects_data = []
            educations_data = []
            certificates_data = []
            skills_data = []

            # Experiences data

            for exp in experiences_data:
                experiences_data.append({
                    "company_name":exp.company_name,
                    "role":exp.role,
                    "role_desc":exp.role_desc,
                    "start_date":exp.start_date,
                    "end_date":exp.end_date
                })

            resume_data["experiences"] =experiences_data
            # Projects data

            for proj in projects_data:
                projects_data.append({
                    "name":proj.name,
                    "desc":proj.desc,
                    "start_date":proj.start_date,
                    "end_date":proj.end_date
                })

            resume_data["projects"] =projects_data
            # Education data

            for edu in educations_data:
                educations_data.append({
                    "school_name":edu.school_name,
                    "degree_name":edu.degree_name,
                    "start_date":edu.start_date,
                    "end_date":edu.end_date
                })

            resume_data["educations"] =educations_data
            # Certificates data

            for cert in certificates_data:
                certificates_data.append({
                    "title":cert.title,
                    "start_date":cert.start_date,
                    "end_date":cert.end_date
                })

            resume_data["certificates"] =certificates_data
            # Skills data

            for ski in skills_data:
                skills_data.append({
                    "title":ski.title,
                    "confidence_score":ski.confidence_score
                })

            resume_data["skills"] =skills_data

            return jsonify(generatedResume=resume_data)

        # db.drop_all()
        db.create_all()
        db.session.commit()

        return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)