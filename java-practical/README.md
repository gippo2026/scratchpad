# Java Practicals

Java laboratory practicals for the course. This directory is the only content
of the standalone **`java-practical`** orphan branch, exactly like
`python-practicals/` lives on `py-practical`.

## Layout

```
java-practical/
├── assignment1/
│   └── setA/
│       └── Q1.java      # starter example
└── .gitignore           # ignores *.class, build dirs, etc.
```

Add further assignments as `assignmentN/setA|setB|setC/Q*.java`.

## Compile and run

From this directory:

```bash
javac assignment1/setA/Q1.java
java -cp assignment1/setA Q1
```

Java is installed via mise (`java@25`, LTS). Check with `java -version`.
No build tool is configured — plain `javac`/`java` keeps the practicals simple.
