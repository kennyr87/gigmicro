const gulp = require('gulp');
const sass = require('gulp-sass');
const cleanCSS = require('gulp-clean-css');
const del = require('del');
const rename = require('gulp-rename');
const parseArgs = require('minimist');

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

// CLI options, use --production to run cleanCSS
const argv = parseArgs(process.argv.slice(2));

const enabled = {
  prodEnabled: argv.production
};

function clean() {
  return del( paths.clean );
}

function styles() {
  let stream = gulp.src( paths.styles.src )
    .pipe(sass());

    if ( enabled.prodEnabled ) {
      stream = stream.pipe(cleanCSS());
    }

    return stream.pipe(rename( 'styles.css' ))
      .pipe(gulp.dest( paths.styles.dest ));
}

async function buildTasks() {
  await clean();
  styles();
}

gulp.task( 'clean', clean );
gulp.task( 'styles', styles );
gulp.task( 'default', buildTasks );
