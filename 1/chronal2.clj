(defn parse-int [number-string]
  (try (Integer/parseInt number-string)
    (catch Exception e nil)))

(defn first-frequency [changes]
  (loop
    [[f & more] changes
     sum 0
     seen #{}]
    (let [x (+ f sum)]
      (if (contains? seen x)
        x
        (recur more x (conj seen x))
        ))))

(println
  (with-open [rdr (clojure.java.io/reader "input.txt")]
    (first-frequency (cycle (map parse-int (line-seq rdr))))))
