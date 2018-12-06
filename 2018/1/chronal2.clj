(defn parse-int [number-string]
  (try (Integer/parseInt number-string)
    (catch Exception e nil)))

(defn first-frequency [[sum seen] change]
    (let [new-sum (+ change sum)]
      (if (contains? seen new-sum)
        (reduced new-sum)
        [new-sum (conj seen new-sum)]
        )))

(println
  (with-open [rdr (clojure.java.io/reader "input.txt")]
    (reduce first-frequency [0 #{}] (cycle (map parse-int (line-seq rdr))))))
