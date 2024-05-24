# 0x03. Unittests and Integration Tests

## Project Overview

- **Category**: UnitTests, Back-end, Integration tests
- **Weight**: 1
- **Start Date**: May 23, 2024, 6:00 AM
- **End Date**: May 28, 2024, 6:00 AM
- **Checker Release Date**: May 24, 2024, 12:00 PM
- **Auto Review**: An auto review will be launched at the deadline

## Introduction

Unit testing is the process of testing that a particular function returns expected results for different sets of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low-level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.
