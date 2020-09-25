from app import db

class CricketFact(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fact = db.Column(db.String, nullable=False, unique=True)
    source = db.Column(db.String)

    @staticmethod
    def add_fact(fact):
        cricket_fact = CricketFact(fact=fact)
        db.session.add(cricket_fact)
        try:
            db.session.commit()
            return CricketFact
        except:
            db.session.rollback()
            return None

    def remove_fact(self):
        cricket_fact = CricketFact.query.filter_by(id=self.id)
        cricket_fact.delete()
        try:
            db.session.commit()
        except:
            db.session.rollback()

    def edit_fact(self, fact):
        cricket_fact = CricketFact.query.filter_by(id=self.id)
        cricket_fact.fact = fact
        try:
            db.session.commit()
        except:
            db.session.rollback()

    @staticmethod
    def does_fact_exist(fact):
        return CricketFact.query.filter_by(fact=fact) != None

    def get_json(self):
        return {
            'id': self.id,
            'fact': self.fact,
        }
