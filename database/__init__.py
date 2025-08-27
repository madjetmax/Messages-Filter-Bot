from sqlalchemy import delete, select, update, insert

# exceptions 

from .engine import session_maker
from .models import Keyword, TriggerName, Phrase

# * triggers
# keywords
async def add_keyword(word: str) -> Keyword:
    async with session_maker() as db_session:
        new_keyword = Keyword(
            word=word
        )
        db_session.add(new_keyword)
        await db_session.commit()

        return new_keyword
    
async def delete_keyword(word_id: int):
    async with session_maker() as db_session:
        query = delete(Keyword).where(Keyword.id==word_id)
        await db_session.execute(query)
        await db_session.commit()

async def get_keyword(word_id: int) -> Keyword:
    async with session_maker() as db_session:
        query = select(Keyword).where(Keyword.id==word_id)
        data = await db_session.execute(query)

        return data.scalars().one()
    
async def get_all_keywords() -> list[Keyword]:
    async with session_maker() as db_session:
        query = select(Keyword)
        data = await db_session.execute(query)

        return data.scalars().all()
    
# trigger names
async def add_trigger_name(name: str) -> TriggerName:
    async with session_maker() as db_session:
        new_trigger_name = TriggerName(
            name=name
        )
        db_session.add(new_trigger_name)
        await db_session.commit()

        return new_trigger_name
    
async def delete_trigger_name(name_id: int):
    async with session_maker() as db_session:
        query = delete(TriggerName).where(TriggerName.id==name_id)
        await db_session.execute(query)
        await db_session.commit()

async def get_trigger_name(name_id: int) -> TriggerName:
    async with session_maker() as db_session:
        query = select(TriggerName).where(TriggerName.id==name_id)
        data = await db_session.execute(query)

        return data.scalars().one()
    
async def get_all_trigger_names() -> list[TriggerName]:
    async with session_maker() as db_session:
        query = select(TriggerName)
        data = await db_session.execute(query)

        return data.scalars().all()
    
# phrases
async def add_phrase(text: str) -> Phrase:
    async with session_maker() as db_session:
        new_phrase = Phrase(
            text=text
        )
        db_session.add(new_phrase)
        await db_session.commit()

        return new_phrase
    
async def delete_phrase(phrase_id: int):
    async with session_maker() as db_session:
        query = delete(Phrase).where(Phrase.id==phrase_id)
        await db_session.execute(query)
        await db_session.commit()

async def get_phrase(phrase_id: int) -> Phrase:
    async with session_maker() as db_session:
        query = select(Phrase).where(Phrase.id==phrase_id)
        data = await db_session.execute(query)

        return data.scalars().one()
    
async def get_all_phrases() -> list[Phrase]:
    async with session_maker() as db_session:
        query = select(Phrase)
        data = await db_session.execute(query)

        return data.scalars().all()