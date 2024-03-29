var browserify = require('browserify');
var watchify = require('watchify');
var gulp = require('gulp');
var gutil = require('gulp-util');
var source = require('vinyl-source-stream');
var reactify = require('reactify');

function bundle(b) {
    gutil.log('Retranspiling source code');
    return b.bundle()
           .pipe(source('main.js'))
           .pipe(gulp.dest('./dist'));
}

function act(watch) {
    var b = browserify({
        debug: true,
        cache: {},
        packageCache: {},
        fullPaths: true
    });
    if (watch) {
        b = watchify(b);
    }
    b.transform(function(file) {
        return reactify(file, {
            harmony: true
        });
    });
    if (watch) {
        b.on('update', function() {
            bundle(b);
        });
    }
    b.add('./main.js');
    bundle(b);
}

gulp.task('watchify', function() {
    act(true);
});

gulp.task('browserify', function() {
    act(false);
});
