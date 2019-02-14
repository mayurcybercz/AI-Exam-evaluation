//IMPORTS
var express = require('express');
var router = express.Router();
var flash = require('connect-flash');

Exam=require('../models/exam');
Image=require('../models/image');
var mongo=require('mongodb');
var assert=require('assert');
//var url='mongodb://localhost:27017';
var spawn=require('child_process').spawn;

// Get Homepage
router.get('/', ensureAuthenticated, function(req, res){
	res.render('index');
});

router.get('/:username', ensureAuthenticated, function(req, res,next){
	res.render('index',{username:req.params.username});
});

//LOGIN CHECK
function ensureAuthenticated(req, res, next){
	if(req.isAuthenticated()){
		return next();
	} else {
		req.flash('error_msg','Session timed out! Please log in again');
		res.redirect('/users/login');
	}
}

//EXAMS
router.post('/:username/exams',function (req, res) {
	var username=req.body.username;
	if(username){
	res.redirect('/'+username+"/exams");
	}
	else{
		res.redirect('/');
	}
});


router.get('/:username/exams', ensureAuthenticated, (req, res) => {
	Exam.getExams((err, examData) => {
		if(err){
			throw err;
		}
		res.render('exams',{exams:examData, username: req.params.username});		
	});
});

module.exports = router;

//ADD EXAM
router.get('/:username/addexam',ensureAuthenticated, function(req,res,next){
	res.render('add_exam',{username:req.params.username});
	console.log('req',req.params);
});

router.post('/:username/addexam',function (req, res) {
	var username=req.body.username;
	if(username){
	res.redirect('/'+username+"/addexam");
	}
	else{
		res.redirect('/');
	}
});

const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/exam');
var db = mongoose.connection;

router.post('/:username/addexam/submit', (req, res) => {
	var username=req.body.username;
	var exam = req.body;
	Exam.addExam(exam, (err, exam) => {
		if(err){
			throw err;
		}
		res.redirect('/'+username+"/exams");
	});
});


//EXAM DETAILS
router.get('/:username/examdetails/:_id', ensureAuthenticated, function(req, res) {
	Exam.getExamById(req.params._id, (err, exam) => {
		if(err){
			throw err;
		}
		res.render('exam_details',{examDetail:exam, username:req.params.username});
		// console.log('req details',req.params.user);
	});
});

// Update Exam
router.get('/:username/editexam/:_id',ensureAuthenticated, (req, res) =>{
	Exam.getExamById(req.params._id, (err, exam) => {
		if(err){
			throw err;
		}
		res.render('edit_exam',{examDetail:exam, username:req.params.username});
	});
});

var methodOverride = require('method-override');
router.use(methodOverride('_method'));

router.put('/:username/editexam/:_id', (req, res) => {
	var username=req.body.username;
	var id = req.params._id;
	var exam = req.body;
	Exam.updateExam(id, exam, {}, (err, exam) => {
		if(err){
			throw err;
		}
		res.redirect('/'+username+"/exams");
		
	});
});

// Remove an Exam
router.get('/:username/deleteexam/:_id',ensureAuthenticated, (req, res) =>{
	Exam.getExamById(req.params._id, (err, exam) => {
		if(err){
			throw err;
		}
		res.render('exams',{username:req.params.username});
	});
});

router.delete('/:username/deleteexam/:_id', (req, res) => {
	var username=req.body.username;
	var id = req.params._id;
	Exam.removeExam(id, (err, exam) => {
		if(err){
			throw err;
		}
		res.redirect('/'+username+"/exams");
	});
});

module.exports = router;

//COURSES
router.post('/:username/courses',function (req, res) {
	var username=req.body.username;
	if(username){
	res.redirect('/'+username+"/courses");
	}
	else{
		res.redirect('/');
	}
});

router.get('/:username/courses',ensureAuthenticated, function(req, res,next){
	res.render('courses',{username:req.params.username});
});

module.exports = router;


//ADMIN TOOLS
router.post('/:username/admin_tools',function (req, res) {
	var username=req.body.username;
	if(username){
	res.redirect('/'+username+"/admin_tools");
	}
	else{
		res.redirect('/');
	}
});

router.get('/:username/admin_tools', ensureAuthenticated, function(req, res,next){
	res.render('admin_tools',{username:req.params.username});
});

module.exports = router;

//OCR

router.post('/:username/admin_tools/ocr',function (req, res) {
	var username=req.body.username;
	if(username){
	res.redirect('/'+username+"/admin_tools/ocr");
	}
	else{
		res.redirect('/');
	}
});

router.get('/:username/admin_tools/ocr', ensureAuthenticated, function(req, res,next){
	res.render('ocr',{username:req.params.username});
});

////
router.get('/:username/admin_tools/ocr', ensureAuthenticated, function(req, res,next){
	Image.index1();
	res.render('ocr',{username:req.params.username});
});

router.get('/:username/admin_tools/ocr/:image_id', ensureAuthenticated, function(req, res,next){
	Image.index();
	res.render('ocr',{username:req.params.username});
});

router.post('/:username/admin_tools/ocr', function(req, res){
    	var username=req.body.username;
    	Image.create();
    	res.redirect('/:username/admin_tools/ocr');	
});

router.delete('/:username/admin_tools/ocr/:image_id', function(req, res){
    	var username=req.body.username;
    	Image.remove;
    	res.redirect('/:username/admin_tools/ocr');	
});
//

module.exports = router;

router.post('/:username/admin_tools/add_new_paper',function (req, res) {
	var username=req.body.username;
	if(username){
	res.redirect('/'+username+"/admin_tools/add_new_paper");
	}
	else{
		res.redirect('/');
	}
});

router.get('/:username/admin_tools/add_new_paper', ensureAuthenticated, function(req, res,next){
	res.render('add_new_paper',{username:req.params.username});
});

module.exports = router;

router.post('/:username/admin_tools/download_pdf',function (req, res) {
	var username=req.body.username;
	if(username){
	res.redirect('/'+username+"/admin_tools/download_pdf");
	}
	else{
		res.redirect('/');
	}
});

router.get('/:username/admin_tools/download_pdf', ensureAuthenticated, function(req, res,next){
	res.render('download_pdf',{username:req.params.username});
});

module.exports = router;

router.post('/:username/admin_tools/check_your_paper',function (req, res) {
	var username=req.body.username;
	if(username){
	res.redirect('/'+username+"/admin_tools/check_your_paper");
	}
	else{
		res.redirect('/');
	}
});

router.get('/:username/admin_tools/check_your_paper', ensureAuthenticated, function(req, res,next){
	res.render('check_your_paper',{username:req.params.username});
});

module.exports = router;


router.post('/:username/admin_tools/check_a_question',function (req, res) {
	var username=req.body.username;
	if(username){
	res.redirect('/'+username+"/admin_tools/check_a_question");
	}
	else{
		res.redirect('/');
	}
});

router.get('/:username/admin_tools/check_a_question', ensureAuthenticated, function(req, res,next){
	res.render('check_a_question',{username:req.params.username});
});

router.post('/:username/admin_tools/check_a_question/submit',function (req, res) {
var script1_output=null;
var process = spawn('python',["'../scripts/test.py'",  
							req.body.question.toString(),
							req.body.answer.toString(),
							req.body.uinput.toString(),
							req.body.keywords.toString()] );

							process.stdout.on('data', function(data) { 
								script1_output=data.toString(); 
							} )


	if(script1_output){
	res.redirect('/'+username+"/admin_tools/check_a_question/"+script1_output);
	}
	else{
		res.redirect('/');
	}
});

router.get("/:username/admin_tools/check_a_question/:script1_output",ensureAuthenticated,function(req,res,next){
	res.render('display_cosine_result',{username:req.params.username,script1_output:req.params.script1_output});
});

module.exports = router;
