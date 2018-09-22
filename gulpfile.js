const gulp = require('gulp');
const sass = require('gulp-sass');
const cleanCSS = require('gulp-clean-css');
const del = require('del');
const rename = require('gulp-rename');

const paths = {
  styles: {
    src: './assets/scss/styles.scss',
    dest: './flask_app/static/dist'
  },
  scripts: {
    src: './assets/scripts/**/*.js',
    dest: './flask_app/static/dist'
  },
  clean: './flask_app/static/dist/*'
};

function clean() {
  return del( paths.clean );
}

function styles() {
  return gulp.src( paths.styles.src )
    .pipe(sass())
    .pipe(cleanCSS())
    .pipe(rename( 'styles.css' ))
    .pipe(gulp.dest( paths.styles.dest ));
}

async function buildTasks() {
  await clean();
  styles();
}

gulp.task( 'clean', clean );
gulp.task( 'styles', styles );
gulp.task( 'default', buildTasks );
