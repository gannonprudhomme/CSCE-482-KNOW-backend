/* eslint-disable import/no-extraneous-dependencies */
import {
  warn, fail, danger,
} from 'danger';

const { github } = danger;
const { pr } = github;

// Modified or created files
const touchedFiles = danger.git.modified_files.concat(danger.git.created_files);


// Checks if the total additions (minus an offset, for ignoring package-lock.json changes)
function checkForBigPR(offset = 0) {
  const bigPRThreshold = 500;
  const changedLines = pr.additions + pr.deletions - offset;
  if (changedLines > bigPRThreshold) {
    warn(`:exclamation: Big PR(${changedLines})! You might want to split this up into`
          + ' separate commits in order to maximize the effectiveness of code review');
  }
}

const pipLockPath = 'Pipfile.lock';
let commitContainsPipLock = false;
touchedFiles.forEach((file) => {
  if (file === pipLockPath) {
    commitContainsPipLock = true;
  }
});

// Check if the PR line count(other than package-lock.json?) is over 500 lines
if (commitContainsPipLock) {
  // Counts the changes in package-lock.json, so that the big PR check doesn't include them
  danger.git.diffForFile(pipLockPath).then((diff) => {
    const changed = diff.added.split('\n').length + diff.removed.split('\n').length;
    checkForBigPR(changed);
  });
} else {
  // Add up the additions normally and check if it's over a certain threshold
  checkForBigPR();
}

// Add a warning if the PR doesn't have an assignee
const someoneAssigned = pr.assignee;
if (someoneAssigned == null) {
  warn('Please assign someone to this PR, such as the creator of the PR or people to'
         + ' review it');
}

// Add a failure if it doens't have a PR description
if (pr.body.length === 0) {
  warn('Please add a PR description');
}

// Add a warning if there aren't any labels on this PR
if (github.issue.labels.length === 0) {
  warn('Please add a label to this PR');
}
