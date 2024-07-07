Axiom test1: forall a b: Prop, (a -> b) -> (~a \/ b). 
Axiom test2: forall a b: Prop, (~a \/ b) -> ~b -> ~a . 
Axiom test3: forall a: Prop, ~~a -> a. 
Axiom test4: forall a: Prop, a -> ~~a. 

Theorem task1: forall (A B: Prop), True -> ((A -> B) <-> (~B -> ~A)).
Proof.
intros.
split.
- intros. tauto.
- intros. apply test1 in H0. 
apply test2 in H0. 
apply test3 in H0. auto. 
apply test4. auto.
Qed.

Axiom conjunction: forall (A B: Prop), A /\ B -> B /\ A.

Theorem task2: forall (A B: Prop), A /\ B <-> B /\ A.
Proof.
split.
- intros. apply conjunction. exact H.
- intros. apply conjunction. exact H.
Qed.

Theorem task3: forall (A B: Prop), True -> ((A -> (A -> B)) -> (A -> B)).
Proof.
intros. 
tauto.
Qed.

Variable A : nat -> Prop.

Theorem task4: (forall x, ~A x) -> ~(exists x, A x).
Proof.
intros H0 H1.
unfold not in H0.
destruct H1.
apply H0 in H.
contradiction.
Qed.