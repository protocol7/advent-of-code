(defn parse-int [number-string]
  (try (Integer/parseInt number-string)
    (catch Exception e nil)))

(println
  (with-open [rdr (clojure.java.io/reader "input.txt")]
    (reduce + (map parse-int (line-seq rdr)))))
