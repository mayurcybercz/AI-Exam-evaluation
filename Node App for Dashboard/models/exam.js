const mongoose = require('mongoose');

// Exam Schema
const examSchema = mongoose.Schema({
	cid:{
		type: String,
		required: true
	},
	eid:{
		type: String,
		required: true
	},
	examName:{
		type: String,
		required: true
	},
	examDate:{
		type: String,
		required: true
	},
	isActive:{
		type: String,
		required: true
	}
});

const Exam = module.exports = mongoose.model('Exam', examSchema);

// Get Exams
module.exports.getExams = (callback, limit) => {
	Exam.find(callback).limit(limit);
}

// Get Exam
module.exports.getExamById = (id, callback) => {
	Exam.findById(id, callback);
}

// Add Exam
module.exports.addExam = (exam, callback) => {
	Exam.create(exam, callback);
}

// Update Exam
module.exports.updateExam = (id, exam, options, callback) => {
	var query = {_id: id};
	var update = {
		cid: exam.cid,
		eid: exam.eid,
		examName: exam.examName,
		examDate: exam.examDate,
		isActive: exam.isActive
	}
	Exam.findOneAndUpdate(query, update, options, callback);
}

// Delete Exam
module.exports.removeExam = (id, callback) => {
	var query = {_id: id};
	Exam.remove(query, callback);
}

